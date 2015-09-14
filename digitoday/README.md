+++ Make unlabeled digitoday data

You probably never need to do this, but:

1. Install hfst,
2. compile omorfi,
3. copy omorfi/src/generated/omorfi.accept.hfst into finer-data/omorfi,
4. make omorfi-tokenizer,
5. cd digitoday && make 