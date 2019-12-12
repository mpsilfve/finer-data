#!/usr/bin/env python

import os
import sys
import re

from collections import defaultdict


NEW_DOC_RE = re.compile('^<HEADLINE>.*')


def group_into_documents(conll_lines):
    documents = []
    current = []
    for line in conll_lines:
        if NEW_DOC_RE.match(line) and current:
            documents.append(current)
            current = []
        current.append(line)
    if current:
        documents.append(current)
    return documents


def main(argv):
    if len(argv) != 2:
        print('Usage: {} FILE'.format(os.path.basename(__file__)),
              file=sys.stderr)
        return 1

    with open(argv[1]) as f:
        lines = [l.rstrip('\n') for l in f]

    documents = group_into_documents(lines)
    for docidx, sentences in enumerate(documents, start=1):
        docid = str(docidx).zfill(3)
        with open('{}.tsv'.format(docid), 'wt') as f:
            for s in sentences:
                print(s, file=f)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
