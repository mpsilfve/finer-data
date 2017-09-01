import sys
import re


for line in sys.stdin:

    line = line.strip()
    if line == '':
        print()
    else:
        line = line.split('\t')
        
        if len(line) == 1:
            word = line[0]
            tag = 'O'
        else:
            word = line[0]
            tag = line[1]
        
        word = re.sub(r'[^a-zåäöA-ZÅÄÖ0-9\.\,\!\?\:\-\_]', '', word)
#        word = re.sub(r'[^A-ZÅÄÖ]', '', word)
#        word = re.sub(r'^(\.\,\!\?\:)', '', word)
        if word != '':
            print(word + '\t' + tag)

    
        
    
