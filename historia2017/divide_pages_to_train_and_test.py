import sys
#import os.path
import os
import csv
import re
import numpy

reload(sys)
sys.setdefaultencoding('UTF-8')

files = [f for f in os.listdir(sys.argv[1] + '/') if os.path.isfile(os.path.join(sys.argv[1] + '/', f))]

for file in files:

    if file[len(file)-4:] != '.csv':
        files.remove(file)

# select N_tran+N_test files randomly
N_train = 135
N_test = 20

if N_train+N_test > len(files):

    print "Not enough files: ", N_train+N_test, '>', len(files)
    exit()

random_indexes = numpy.random.permutation(len(files))[:N_train+N_test]

for i in range(N_train):

    os.system('cp ' + sys.argv[1] + files[i] + ' ' + sys.argv[2])

for i in range(N_train,N_train+N_test):

    os.system('cp ' + sys.argv[1] + files[i] + ' ' + sys.argv[3])









