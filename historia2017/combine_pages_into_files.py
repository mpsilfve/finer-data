# this is obsolete


import sys
#import os.path
import os
import random
import csv
import re

reload(sys)
sys.setdefaultencoding('UTF-8')

files = [f for f in os.listdir(sys.argv[1] + '/') if os.path.isfile(os.path.join(sys.argv[1] + '/', f))]

line_num = 0
package_num = 0
data_out = []

for file_in in files:

    if file_in[len(file_in)-4:] != '.csv':
        continue

    # read raw page in
    data_in = list(csv.reader(open(sys.argv[1] + '/' + file_in, 'rb'), delimiter='\t', quotechar='', quoting=csv.QUOTE_NONE, escapechar=''))

    for line in data_in:

        data_out.append(line)
        line_num += 1

    if line_num > 5000:
        
        print file_in, sys.argv[2] + '/set' + str(package_num) + '.csv', line_num
        FILE = open(sys.argv[2] + '/set' + str(package_num) + '.csv', 'w')
        csvwriter = csv.writer(FILE, delimiter='\t', quotechar='', quoting=csv.QUOTE_NONE, escapechar='')
        for line in data_out:
            csvwriter.writerow(line)
        FILE.close()

        data_out = []

        package_num += 1
        line_num = 0



