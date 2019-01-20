all:test_data_section_text test_bisnes_section_text test_mobiili_section_text \
test_tyo_ja_ura_section_text test_tietoturva_section_text test_tiede_ja_teknologia_section_text \
test_vimpaimet_section_text test_yhteiskunta_section_text train_data_section_text \
train_bisnes_section_text train_mobiili_section_text train_tyo_ja_ura_section_text \
train_tietoturva_section_text train_tiede_ja_teknologia_section_text \
train_vimpaimet_section_text train_yhteiskunta_section_text

test_%_text:article_test_data/%
	for f in `ls $^/ | sed 's/\.html//'`; do cat $^/"$$f".html | bin/article2ner.sh > ner_test_data/$*/"$$f".txt; done

train_%_text:article_train_data/%
	for f in `ls $^/ | sed 's/\.html//'`; do cat $^/"$$f".html | bin/article2ner.sh > ner_train_data/$*/"$$f".txt; done



