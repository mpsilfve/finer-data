# -*- coding: utf-8 -*-

import sys
#import os.path
import os
import random
import csv
import re

reload(sys)
sys.setdefaultencoding('UTF-8')


# loop files in directory sys.argv[1]

files = [f for f in os.listdir(sys.argv[1] + '/') if os.path.isfile(os.path.join(sys.argv[1] + '/', f))]

for file_in in files:

    if file_in[len(file_in)-4:] != '.csv':
        continue

    # read raw page in
    data_in = list(csv.reader(open(sys.argv[1] + '/' + file_in, 'rb'), delimiter='\t', quotechar='', quoting=csv.QUOTE_NONE, escapechar=''))
    word_index = int(sys.argv[2]) # which column to write out (counting from zero)
    
    print '<FILENAME>' + '\n' + file_in[:-4] + '\n'

    for line_index in range(0, len(data_in)):

        print data_in[line_index][word_index]
#        print data_in[line_index][word_index], data_in[line_index][word_index+1] # print also the possible annotation at column word_index

    print
