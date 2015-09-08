all:data_section_text bisnes_section_text

%_text:article_data/%
	for i in `seq 0 40`; do cat $^/"$$i".html | bin/article2ner.sh > ner_data/$*/"$$i".txt; done