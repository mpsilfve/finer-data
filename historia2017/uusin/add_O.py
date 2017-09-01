import sys

for word in sys.stdin:
    word = word.strip()
    if word == '':
        print(word)
    else:
        print(word + '\t' + 'O')



