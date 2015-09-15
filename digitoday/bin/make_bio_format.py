#! /usr/bin/env python3

from sys import stdin
from re import match

def is_start_tag(tag):
    if tag != '':
        return tag[0] == 'b'
    return 0

def get_elem(tag):
    if tag != '':
        if tag[0] == 'b':
            tag = tag[1:]
        return tag.upper()
    return 'O'

pelem = 'O'
    
for line in stdin:
    line = line.strip()

    elem = 'O'
    start = 0

    if line == '':
        print()
        pelem = 'O'
    elif match('<.*>', line):
        print(line)
    elif not '\t' in line:
        print('%s\t%s' % (line, 'O'))
        pelem = 'O'
    else:
        word, label = line.split('\t')
        elem = get_elem(label)
        start = is_start_tag(label)

        if elem == 'O':
            print('%s\t%s' % (word, 'O'))
            pelem = 'O'
        else:
            if elem == pelem:
                if start:
                    print('%s\tB-%s' % (word, elem))
                else:
                    print('%s\tI-%s' % (word, elem))
            else:
                print('%s\tB-%s' % (word, elem))

        pelem = elem
