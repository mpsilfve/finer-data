#PATH_TO_STANFORD_NER=../../stanford-ner-2016-10-31
PATH_TO_STANFORD_NER=../../../Downloads/stanford-ner-2016-10-31

#comment

gt-loc-per-model.ser.gz:train.gt.csv
	java -Xmx12000M -cp $(PATH_TO_STANFORD_NER)/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop conf-loc-per

gt-org-model.ser.gz:train.gt.csv
	java -Xmx12000M -cp $(PATH_TO_STANFORD_NER)/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop conf-org

gt-sent-extractor-model.ser.gz:train.gt.sent.csv
	java -Xmx12000M -cp $(PATH_TO_STANFORD_NER)/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop conf-sent

#ocr-model.ser.gz:gt.csv
#	java -Xmx12000M -cp $(PATH_TO_STANFORD_NER)/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop conf.ocr


#hist-model.ser.gz:train_hist.csv
#	java -Xmx12000M -cp $(PATH_TO_STANFORD_NER)/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop conf.hist

#finer-model.ser.gz:dataset/digitoday.train+dev wikipedia_gazette w2v_gazette omorfi_gazette
#	java -Xmx12000M -cp $(PATH_TO_STANFORD_NER)/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop conf

#finer-model-no-pos.ser.gz:no_pos_train+dev wikipedia_gazette w2v_gazette omorfi_gazette
#	java -Xmx12000M -cp $(PATH_TO_STANFORD_NER)/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop no_pos_conf

#test.sys:finer-model.ser.gz test
#	java -cp $(PATH_TO_STANFORD_NER)/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier finer-model.ser.gz -testFile test > test.sys

#no_pos_test.sys:finer-model-no-pos.ser.gz no_pos_test
#	java -cp $(PATH_TO_STANFORD_NER)/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier finer-model-no-pos.ser.gz -testFile no_pos_test > no_pos_test.sys

#test.eval:test.sys
#	python3 eval.py $^ > $@