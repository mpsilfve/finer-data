#!/usr/bin/env python3

# Merge formatting tags (e.g. "<BODY>") from one TSV file into another
# that lacks them.

import sys
import re

from itertools import zip_longest


TAG_RE = re.compile(r'^<(DATE|HEADLINE|INGRESS|BODY|PARAGRAPH)>(.*)')


def argparser():
    from argparse import ArgumentParser
    ap = ArgumentParser()
    ap.add_argument('tagged', help='File without tags')
    ap.add_argument('untagged', help='File with tags')
    return ap


def parse_tsv(fn):
    sentences, tags, lines = [], [], []
    with open(fn) as f:
        for ln, l in enumerate(f, start=1):
            l = l.rstrip('\n')
            m = TAG_RE.match(l)
            if l.isspace() or not l:
                if lines:
                    sentences.append((tags, lines))
                    tags, lines = [], []
            elif m:
                if m.group(1) != 'DATE':    # ignore date
                    tags.append('<{}>'.format(m.group(1)))
            else:
                lines.append(l)
    if lines:
        sentences.append((tags, lines))
    return sentences


def main(argv):
    args = argparser().parse_args(argv[1:])
    tagged = parse_tsv(args.tagged)
    untagged = parse_tsv(args.untagged)
    print('read {} tagged, {} untagged sentences'.format(
        len(tagged), len(untagged)), file=sys.stderr)
    assert len(tagged) == len(untagged), 'length mismatch'
    for (tags, t_lines), (_, u_lines) in zip(tagged, untagged):
        for tag in tags:
            print(tag, end='\n\n')
        for t_line, u_line in zip_longest(t_lines, u_lines):
            t_tok = '' if t_line is None else t_line.split('\t')[0]
            u_tok = '' if u_line is None else u_line.split('\t')[0]
            t_tok = t_tok.replace(' ', '\\_')
            if t_tok != u_tok:
                print('warning: token mismatch: {} vs {}'.format(t_tok, u_tok),
                      file=sys.stderr)
            print(u_line)
        print()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

