import sys
import csv

reload(sys)
sys.setdefaultencoding('UTF-8')


def quote(col):
    if col is None:
        return ''
    return '"{}"'.format(str(col).replace('""', ''))


# read csv data in from sys.argv[1]
#data = list(csv.reader(open(sys.argv[1], 'rb'), delimiter='\t', quotechar='"', quoting=csv.QUOTE_NONE))
data = list(csv.reader(open(sys.argv[1], 'rb'), delimiter='\t', quoting=csv.QUOTE_NONE, quotechar='', escapechar=''))
#data = list(csv.reader(open(sys.argv[1], 'rb'), delimiter='\t'))


prev_page_index = None
prev_year = None
page_data = None
line_num = 0

for line in data:

    if line_num == 0:

        line_num = 1
        continue

    page_index = line[3]
    year = line[1]
    
    if page_index != prev_page_index and page_data == None:

        page_data = [line]

    elif page_index != prev_page_index and page_data != None and int(prev_year) > 1910: 

        page_data = [line]

    elif page_index != prev_page_index and page_data != None:
        
#        FILE = open(sys.argv[2] + '/' + prev_page_index + '.csv', 'w')
#        for line in page_data:
#            FILE.write('\t'.join(line) + '\n')
#        FILE.close()

        FILE = open(sys.argv[2] + '/' + prev_page_index + '.csv', 'w')
#        csvwriter = csv.writer(FILE, delimiter='\t', quotechar='"', quoting=csv.QUOTE_NONE)
        csvwriter = csv.writer(FILE, delimiter='\t', quotechar='', quoting=csv.QUOTE_NONE, escapechar='')
        for line in page_data:
#            print line
            csvwriter.writerow(line)
        FILE.close()

        page_data = [line]

    else:

        page_data.append(line)

    prev_page_index = page_index
    prev_year = year
    line_num += 1

 



