import sys
import numpy
from collections import Counter


# read data
lines = []
for line in sys.stdin:
    lines.append(line.strip())
#    print(line)


entity_types = []

# 
#myfile = open(sys.argv[1], 'r')
mydata = []
entity = ''
entities = []
mycounts = Counter()
t = 0
for line in lines:

    if line == '':
        
        if entity != '':
            entities.append(entity)
            entity = ''
        
        mydata.append(entities)
        t = 0
        entities = []

    else:
            
        line = line.split('\t')

        word = line[0].strip()
        tag = line[2].strip()

        if tag[:2] == 'B-' and entity == '':
            entity = '%s %d' % (tag, t)
            entity_type = tag[2:]
            if entity_type not in entity_types:
                entity_types.append(entity_type)
            mycounts[entity_type] += 1
        elif tag[:2] == 'B-' and entity != '':
            entities.append((entity, entity_type))
            entity = '%s %d' % (tag, t)
            entity_type = tag[2:]
            if entity_type not in entity_types:
                entity_types.append(entity_type)
            mycounts[entity_type] += 1
        elif tag[:2] == 'I-':
            entity += ' %s %d' % (tag, t)
        elif tag == 'O' and entity != '':
            entities.append((entity, entity_type))
            entity = ''

        t += 1
    
mydata.append(entities)

#myfile.close()


# 
#goldfile = open(sys.argv[2], 'r')
golddata = []
entity = ''
entities = []
goldcounts = Counter()
t = 0
for line in lines:

    if line == '':
        
        if entity != '':
            entities.append(entity)        
            entity = ''
        
        golddata.append(entities)
        t = 0
        entities = []

    else:
            
        line = line.split('\t')

        word = line[0].strip()
        tag = line[1].strip()

        if tag[:2] == 'B-' and entity == '':
            entity = '%s %d' % (tag, t)
            entity_type = tag[2:]
            if entity_type not in entity_types:
                entity_types.append(entity_type)
            goldcounts[entity_type] += 1
        elif tag[:2] == 'B-' and entity != '':
            entities.append((entity, entity_type))
            entity = '%s %d' % (tag, t)
            entity_type = tag[2:]
            if entity_type not in entity_types:
                entity_types.append(entity_type)
            goldcounts[entity_type] += 1
        elif tag[:2] == 'I-':
            entity += ' %s %d' % (tag, t)
        elif tag == 'O' and entity != '':
            entities.append((entity, entity_type))
            entity = ''

        t += 1

golddata.append(entities)
    
#goldfile.close()


# pre
total = Counter()
correct = Counter()
for i in range(len(mydata)):

    myentities = mydata[i]
    goldentities = golddata[i]

    for myentity in myentities:
        myentity_type = myentity[1]
        if myentity in goldentities:
            correct[myentity_type] += 1
            correct['Totals'] += 1
        total[myentity_type] += 1
        total['Totals'] += 1

pre = {}
for entity_type in total.keys():
    pre[entity_type] = float(correct[entity_type])/float(total[entity_type])
#    print(entity_type, '%.4f' % pre[entity_type])


# total gold entities including those missed by OCR
total = {} 
total['LOC'] = 1826
total['PER'] = 1205
total['ORG'] = 487
total['Totals'] = total['LOC']+total['PER']+total['ORG']

# rec
correct = Counter()
for i in range(len(mydata)):
    myentities = mydata[i]
    goldentities = golddata[i]

    for goldentity in goldentities:
        goldentity_type = goldentity[1]
        if goldentity in myentities:
            correct[goldentity_type] += 1
            correct['Totals'] += 1
#        total[goldentity_type] += 1
#        total['Totals'] += 1

rec = {}
for entity_type in total.keys():
    rec[entity_type] = float(correct[entity_type])/float(total[entity_type])
#    print(entity_type, '%.4f' % pre[entity_type])



#

mycounts['Totals'] = mycounts['LOC']+mycounts['PER']+mycounts['ORG']
# goldcounts['Totals'] = goldcounts['LOC']+goldcounts['PER']+goldcounts['ORG']
goldcounts = total

entity_types = sorted(entity_types)
entity_types.append('Totals')

# f1
f1 = {}
print('Entity\tPre\tRec\tF1\t#my\t#gold')
for entity_type in entity_types:
    f1[entity_type] = 2*pre.get(entity_type, -1)*rec.get(entity_type, -1)/(pre.get(entity_type, -1)+rec.get(entity_type, -1))
    print('%s\t%.4f\t%.4f\t%.4f\t%d\t%d' % (entity_type, pre.get(entity_type, -1), rec.get(entity_type, -1), f1.get(entity_type, -1), mycounts.get(entity_type, -1), goldcounts.get(entity_type, -1)))


