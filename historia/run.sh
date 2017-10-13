GT="gt.annotated"
OCR="ocr.annotated"

# make train and test sets (LOC and PER)
head -n 181456 $GT.csv | cut -f 1,2 > train.gt.csv 
head -n 100000 gt.semi-manually-annotated.csv | cut -f 1,2 >> train.gt.csv
tail -n +181458 $GT.csv | cut -f 1,2 > test.gt.csv # last 34/170 pages

tail -n +172999 $OCR.csv | cut -f 1,2 > test.ocr.csv # last 34/170 pages

# train

Make gt-model.ser.gz

# tag
java -cp ../../../Downloads/stanford-ner-2016-10-31/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier gt-model.ser.gz -testFile test.gt.csv > gt+gt-loc-per.log
java -cp ../../../Downloads/stanford-ner-2016-10-31/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier gt-model.ser.gz -testFile test.ocr.csv > gt+ocr-loc-per.log
 
#rm gt-model.ser.gz

# evaluate with my evaluate.py
cat gt+gt-loc-per.log | python evaluate_offset.py
cat gt+ocr-loc-per.log | python evaluate_offset.py





# make train and test sets (ORG)
head -n 181456 $GT.csv | cut -f 1,3 > train.gt.csv 
head -n 100000 gt.semi-manually-annotated.csv | cut -f 1,3 >> train.gt.csv
tail -n +181458 $GT.csv | cut -f 1,3 > test.gt.csv # last 34/170 pages

tail -n +172999 $OCR.csv | cut -f 1,3 > test.ocr.csv # last 34/170 pages

# train

Make gt-model.ser.gz

# tag
java -cp ../../../Downloads/stanford-ner-2016-10-31/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier gt-model.ser.gz -testFile test.gt.csv > gt+gt-org.log
java -cp ../../../Downloads/stanford-ner-2016-10-31/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier gt-model.ser.gz -testFile test.ocr.csv > gt+ocr-org.log
 
# evaluate with my evaluate.py
cat gt+gt-org.log | python evaluate_offset.py
cat gt+ocr-org.log | python evaluate_offset.py

rm gt-model.ser.gz




# counts from all data
echo "count from all GT data (LOC, PER, ORG)"
grep "B-LOC" $GT.csv | wc -l
grep "B-PER" $GT.csv | wc -l
grep "B-ORG" $GT.csv | wc -l
echo "count from all OCR data (LOC, PER, ORG)"
grep "B-LOC" $OCR.csv | wc -l
grep "B-PER" $OCR.csv | wc -l
grep "B-ORG" $OCR.csv | wc -l



# counts from test data
echo "count from test GT data (LOC, PER, ORG)"
grep "B-LOC" test.gt.csv | wc -l
grep "B-PER" test.gt.csv | wc -l
grep "B-ORG" test.gt.csv | wc -l
echo "count from test OCR data (LOC, PER, ORG)"
grep "B-LOC" test.ocr.csv | wc -l
grep "B-PER" test.ocr.csv | wc -l
grep "B-ORG" test.ocr.csv | wc -l









# =======================================================================================================================


# make gt.csv

#head -n 250424 groundtruth6.csv | grep "<FILENAME>" | cut -f 2 > filenames
#head -n 250424 groundtruth6.csv | sed -e "s/<FILENAME>.*//g" | python3 remove_special_chars.py | tail -n +2 > gt.csv 


# make ocr.csv

#python3 make_ocr_csv.py | python3 remove_special_chars.py | cut -f 1 | python3 tokenize1.py | python3 tokenize2.py| python3 add_O.py > ocr.words.csv

# opeta stanford train.gt:llä

#Make gt-model.ser.gz

# käytä train.gt-stanfordia ocr.csv:ään
#cat ocr.words.csv | sed -e "s/FILENAME.*//g" > tmp
#java -cp ../../../../Downloads/stanford-ner-2016-10-31/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier gt-model.ser.gz -testFile tmp > tmp2
#cut -f 1,3 tmp2 > ocr.csv
#rm tmp tmp2





