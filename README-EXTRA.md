Extra processing steps on top of released version of data

Add section tags (`<HEADLINE>` etc.) into data

```
python3 scripts/mergetags.py \
    legacy-data/digitoday/ner_train_data_annotated/train_publish.csv \
    data/digitoday.2014.csv \
    > data/digitoday.2014.withtags.csv
```

(digitoday.2015.test.csv and wikipedia.test.csv already contain
`<HEADLINE>` tags.)

Create version with `-DOCSTART-` lines

```
egrep -v '^<(BODY|INGRESS|PARAGRAPH)>' data/digitoday.2014.withtags.csv \
    | cat -s | perl -pe 's/<HEADLINE>.*/-DOCSTART-\tO\tO/' \
    > data/digitoday.2014.withdocstart.csv
for f in data/digitoday.2015.test.csv data/wikipedia.test.csv ; do
    egrep -v '^<(BODY|INGRESS|PARAGRAPH)>' $f | cat -s \
        | perl -pe 's/<HEADLINE>.*/-DOCSTART-\tO\tO/' \
	> ${f%.csv}.withdocstart.csv
done
```

Split version of digitoday.2014 (train+dev) with `-DOCSTART-` lines
into train and dev. (Extra `-DOCSTART-` line added for dev start as
the original split is document-internal and lacks `<HEADLINE>`.)

```
head -n 195447 data/digitoday.2014.withdocstart.csv > data/digitoday.2014.train.withdocstart.csv
(echo "-DOCSTART-"$'\t'"O"$'\t'"O"; echo; tail -n +195448 data/digitoday.2014.withdocstart.csv) > data/digitoday.2014.dev.withdocstart.csv
```

Split by document using `<HEADLINE>` tag

digitoday.2014 (train+dev)

```
mkdir data/digitoday.2014.split
cd data/digitoday.2014.split
python3 ../../scripts/split_by_document.py ../digitoday.2014.withtags.csv 
cd -
```

digitoday.2015.test and wikipedia.test (in- and out-of-domain test sets)

```
for s in digitoday.2015.test wikipedia.test; do
    mkdir data/$s.split
    cd data/$s.split
    python3 ../../scripts/split_by_document.py ../$s.csv 
    cd -
done
```

Check splits

```
diff data/digitoday.2014.withtags.csv <(cat data/digitoday.2014.split/*.tsv)
for s in digitoday.2015.test wikipedia.test; do
    diff data/$s.csv <(cat data/$s.split/*.tsv)
done
```

Convert into standoff

```
for s in digitoday.2014 digitoday.2015.test wikipedia.test; do
    mkdir data/$s.standoff
    cd data/$s.standoff/
    for f in ../$s.split/*.tsv; do
        python3 ../../scripts/conll2standoff.py $f \
	    | egrep -v '^T[0-9]+'$'\t' > $(basename $f .tsv).txt
	python3 ../../scripts/conll2standoff.py <(cut -f 1,2 $f) \
	    | egrep '^T[0-9]+'$'\t' > $(basename $f .tsv).ann
	python3 ../../scripts/conll2standoff.py <(cut -f 1,3 $f) \
	    | egrep '^T[0-9]+'$'\t' | perl -pe 's/^T/T10000/' \
	    >> $(basename $f .tsv).ann
    done
    cd -
done
```

Check text

```
for s in digitoday.2014 digitoday.2015.test wikipedia.test; do
    for f in data/$s.split/*.tsv; do
        diff <(cut -f 1 $f | egrep -v '^<[A-Z]+>' | egrep .) \
             <(tr ' ' '\n' < data/$s.standoff/$(basename $f .tsv).txt)
    done
done
```

Check annotation counts

```
for s in digitoday.2014 digitoday.2015.test wikipedia.test; do
    for f in data/$s.split/*.tsv; do
        diff <(cut -f 2,3 $f | tr '\t' '\n' | egrep '^B-' | wc -l) \
             <(egrep '^T' data/$s.standoff/$(basename $f .tsv).ann | wc -l)
    done
done
```

All good.
