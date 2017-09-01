import sys

for word in sys.stdin:

    word = word.strip()
    
    # tokenize prefix
    word = word[::-1]
    tokens = []
    while(True):        
        if len(word) > 1:
            if word[-1] in ['.', ',', '!', '?', ':']:
                tokens.append(word[-1])
                word = word[:-1]
            else:
                break
        else:
            break

    for token in tokens:
        print(token)

    word = word[::-1]

    # tokenize suffix
    tokens = []
    while(True):        
        if len(word) > 1:
            if word[-1] in ['.', ',', '!', '?', ':']:
                tokens.append(word[-1])
                word = word[:-1]
            else:
                break
        else:
            break
    
    if word != '':
        print(word)
    for token in tokens[::-1]:
        print(token)
                
