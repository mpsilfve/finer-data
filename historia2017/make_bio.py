import sys

words = []
tags = []


prev_tag = 'NONE'

for line in sys.stdin:

    line = line.strip().split('\t')

    if len(line) == 1:

        word = line[0]
        tag = ''

    else:

        word = line[0]
        tag = line[1]

    words.append(word.strip())

    tag = tag.strip().upper()

    if tag == '':

        tags.append('O')

    elif tag[0] == 'B':

        tags.append('B-' + tag[1:])
        tag = tag[1:]

    elif tag != prev_tag:

        tags.append('B-' + tag)

    else:

        tags.append('I-' + tag)

    prev_tag = tag

words.append('<NONE>')
tags.append('<NONE>')





for i in range(len(words)-1):

    prev_word = words[i-1]
    prev_tag = tags[i-1]

    this_word = words[i]
    this_tag = tags[i]

    next_word = words[i+1]
    next_tag = tags[i+1]

    if prev_word == '<FILENAME>' or next_word == '<FILENAME>' or this_word == '<FILENAME>':

        continue

    elif this_word == '':

        this_tag = ''

#    elif this_tag == '':

#        this_tag = 'O'

    print this_word + '\t' + this_tag


    
    
