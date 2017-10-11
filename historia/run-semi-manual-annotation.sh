

# preprocess (apply this command when tagging DIGI)
#tail -n +271457 gt.all.csv | python3 remove_empty_lines.py | grep -v -e '^$' | sed 's/^<FILENAME>.*//g' | python3 remove_special_chars.py | python3 tokenize1.py | python3 tokenize2.py | python3 add_O.py > temp
tail -n +101180 .csv | cut -f 1 | python3 add_O.py > temp


GT="gt.annotated.csv"

# train and tag

cut -f 1,2 $GT > train.gt.csv # LOC and PER
echo "" >> train.gt.csv
head -n 101178 gt.semi-manually-annotated.csv | cut -f 1,2 >> train.gt.csv 
Make gt-model.ser.gz
java -cp ../../../Downloads/stanford-ner-2016-10-31/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier gt-model.ser.gz -testFile temp | cut -f 1,3 > temp.loc.per.csv

rm gt-model.ser.gz

cut -f 1,3 $GT > train.gt.csv # ORG
echo "" >> train.gt.csv
head -n 101178 gt.semi-manually-annotated.csv | cut -f 1,3 >> train.gt.csv 
Make gt-model.ser.gz
java -cp ../../../Downloads/stanford-ner-2016-10-31/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier gt-model.ser.gz -testFile temp | cut -f 3 > temp.org.csv

rm gt-model.ser.gz

# combine

paste temp.loc.per.csv temp.org.csv > gt.semi-manually-annotated.csv

rm temp.loc.per.csv
rm temp.org.csv



