# -*- coding: utf-8 -*-

import sys
#import os.path
import os
import random
import csv
import re

reload(sys)
sys.setdefaultencoding('UTF-8')


files = [f for f in os.listdir(sys.argv[1] + '/') if os.path.isfile(os.path.join(sys.argv[1] + '/', f))]

word_index = int(sys.argv[2]) # which column to read in

d = {}

for file_in in files:

    if file_in[len(file_in)-4:] != '.csv':
        continue

    # read raw page in
    data_in = list(csv.reader(open(sys.argv[1] + '/' + file_in, 'rb'), delimiter='\t', quotechar='', quoting=csv.QUOTE_NONE, escapechar=''))
    
    for line in data_in:

        word = line[word_index]
        if word[-1] == '.':
            
            if word not in d:

                d[word] = True
                

for key, val in d.items():

    print key


            
