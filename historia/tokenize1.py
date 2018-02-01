# first tokenizer for ocr text

import sys
import re

for word in sys.stdin:

    word = word.strip()

    word = re.sub(r'[^a-zåäöA-ZÅÄÖ0-9\.\,\!\?\:\-\_]', '', word)

    if word == '':
        print()
    else:
        tokens = word.replace('.', ' . ').replace(',', ' , ').split()
        for token in tokens:
            subtokens = re.sub(r'([a-zåäö])([A-ZÅÄÖ])', r'\1 \2', token).split()
            for subtoken in subtokens:
                print(subtoken)
