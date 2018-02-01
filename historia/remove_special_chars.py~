import sys
import re


for line in sys.stdin:

    line = line.strip()
    if line == '':
        print()
    else:
        line = re.sub(r'[^a-zåäöA-ZÅÄÖ0-9\.\,\!\?\:\-\_]', '', line)
#        word = re.sub(r'[^A-ZÅÄÖ]', '', word)
#        word = re.sub(r'^(\.\,\!\?\:)', '', word)
        if line != '':
            print(line)

    
        
    
