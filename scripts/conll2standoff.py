#!/usr/bin/env python

# Convert a CoNLL-like BIO-formatted entity-tagged file into
# brat-flavored standoff and a reconstruction of the original text.


import codecs
import os
import re
import sys

INPUT_ENCODING = 'UTF-8'
OUTPUT_ENCODING = "UTF-8"

output_directory = None


def tagstr(start, end, ttype, idnum, text):
    # sanity checks
    assert '\n' not in text, "ERROR: newline in entity '%s'" % (text)
    assert text == text.strip(), "ERROR: tagged span contains extra whitespace: '%s'" % (text)
    return "T%d\t%s %d %d\t%s" % (idnum, ttype, start, end, text)


def output(infn, docnum, sentences):
    global output_directory

    if output_directory is None:
        txtout = sys.stdout
        soout = sys.stdout
    else:
        outfn = os.path.join(output_directory, 'doc-{}'.format(docnum))
        txtout = codecs.open(outfn + '.txt', 'w', encoding=OUTPUT_ENCODING)
        soout = codecs.open(outfn + '.ann', 'w', encoding=OUTPUT_ENCODING)

    offset, idnum = 0, 1

    doctext = ""

    for si, sentence in enumerate(sentences):

        prev_token = None
        curr_start, curr_type = None, None

        for token, ttag, ttype in sentence:

            if curr_type is not None and (ttag != "I" or ttype != curr_type):
                # a previously started tagged sequence does not
                # continue into this position.
                print(tagstr(
                    curr_start, offset, curr_type, idnum, doctext[curr_start:offset]), file=soout)
                idnum += 1
                curr_start, curr_type = None, None

            if prev_token is not None:
                doctext = doctext + ' '
                offset += 1

            if curr_type is None and ttag != "O":
                # a new tagged sequence begins here
                curr_start, curr_type = offset, ttype

            doctext = doctext + token
            offset += len(token)

            prev_token = token

        # leftovers?
        if curr_type is not None:
            print(tagstr(
                curr_start, offset, curr_type, idnum, doctext[curr_start:offset]), file=soout)
            idnum += 1

        if si + 1 != len(sentences):
            doctext = doctext + '\n'
            offset += 1

    print(doctext, file=txtout)


def process(fn):
    docnum = 1
    sentences = []

    with codecs.open(fn, encoding=INPUT_ENCODING) as f:
        # store (token, BIO-tag, type) triples for sentence
        current = []
        lines = f.readlines()
        for ln, l in enumerate(lines):
            l = l.strip()
            if re.match(r'^\s*$', l):
                # blank lines separate sentences
                if len(current) > 0:
                    sentences.append(current)
                current = []
                continue
            elif re.match(r'^<(HEADLINE|INGRESS|BODY|PARAGRAPH)>', l):
                # skip 
                continue
            # Assume it's a normal line with token and tag separated
            # by space.
            m = re.match(r'^(\S+)\s(\S+)', l)
            assert m, "Error parsing line %d: %s" % (ln + 1, l)
            token, tag = m.groups()

            # parse tag
            m = re.match(r'^([BIO])((?:-[A-Za-z_]+)?)$', tag)
            assert m, "ERROR: failed to parse tag '%s' in %s" % (tag, fn)
            ttag, ttype = m.groups()
            if len(ttype) > 0 and ttype[0] == "-":
                ttype = ttype[1:]

            current.append((token, ttag, ttype))

        # process leftovers, if any
        if len(current) > 0:
            sentences.append(current)
        if len(sentences) > 0:
            output(fn, docnum, sentences)


def main(argv):
    global output_directory

    # Take an optional "-o" arg specifying an output directory for the results
    output_directory = None
    filenames = argv[1:]
    if len(argv) > 2 and argv[1] == "-o":
        output_directory = argv[2]
        print("Writing output to %s" % output_directory, file=sys.stderr)
        filenames = argv[3:]

    fail_count = 0
    for fn in filenames:
        try:
            process(fn)
        except Exception as e:
            print("Error processing %s: %s" % (fn, e), file=sys.stderr)
            fail_count += 1

    if fail_count > 0:
        print("""
##############################################################################
#
# WARNING: error in processing %d/%d files, output is incomplete!
#
##############################################################################
""" % (fail_count, len(filenames)), file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
