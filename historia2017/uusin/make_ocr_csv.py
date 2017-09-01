import sys


filenames = []
f = open('filenames', 'r')
for line in f:
    filename = line.strip()
    filenames.append(filename)
f.close()

for filename in filenames:
    f = open('tescomb/' + filename + '.txt', 'r', encoding='latin1')
    print("<FILENAME>" + filename)
    for line in f:
        line = line.strip()
        print(line)
    f.close()
    print()
