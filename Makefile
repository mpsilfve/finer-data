all:omorfi/tokenize.hfst digitoday 

digitoday:omorfi/tokenize.hfst
	make -C digitoday

omorfi/tokenize.hfst:omorfi/omorfi.accept.hfst omorfi/tokenize.pmatch
	hfst-pmatch2fst omorfi/tokenize.pmatch > omorfi/tokenize.hfst