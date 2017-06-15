import sys

words = []
tags = []


prev_tag = 'NONE'

for line in sys.stdin:

    line = line.strip().split('\t')

    if len(line) == 1:

        word = line[0].strip()
        tag = ''

    else:

        word = line[0].strip()
        tag = line[1].strip()

    if word == '\xc2\x97' or word == '':
        continue

    words.append(word)

#    tag = tag.upper()

    if tag in ['B-PER', 'I-PER', 'B-ORG', 'I-ORG', 'B-LOC', 'I-LOC', 'B-MISC', 'I-MISC']:

        tags.append(tag)

    elif word == '<FILENAME>':

        tags.append(tag)

    elif tag == '':

        tags.append('') # OUTSIDE
            
    elif tag[0].upper() == 'B':

        tags.append('B-' + tag[1:].upper())
#        tag = tag[1:]

    elif tag != prev_tag:

        tags.append('B-' + tag.upper())

    else:

        tags.append('I-' + tag.upper())

    prev_tag = tag

words.append('<NONE>')
tags.append('<NONE>')



for i in range(len(words)-1):

#    prev_word = words[i-1]
#    prev_tag = tags[i-1]

    this_word = words[i]
    this_tag = tags[i]

#    next_word = words[i+1]
#    next_tag = tags[i+1]

#    if prev_word == '<FILENAME>' or next_word == '<FILENAME>' or this_word == '<FILENAME>':

#        print this_word + '\t' + this_tag
#        print
#        continue

#        this_tag = ''
#        continue

#    else:

#    elif this_tag == '':

#        this_tag = 'O'

    print this_word + '\t' + this_tag


    
    
