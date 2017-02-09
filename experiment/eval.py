from sys import argv, stderr, stdout
from collections import defaultdict as ddict

discard_types = ['MISC']

def get_elem_type(string):
    return string[2:]

def get_elements(data):
    elems = set()
    elem_start = -1
    elem_type = None
    for i, e in enumerate(data):
        wf, label = e
        if wf =='':
            if elem_start != -1:
                if not elem_type in discard_types:
                    elems.add((elem_start, i, elem_type))
            elem_start = -1
            elem_type = None
        else:
            if label[0] == 'B':
                if elem_start != -1:
                    if not elem_type in discard_types:
                        elems.add((elem_start, i, elem_type))
                elem_start = i
                elem_type = get_elem_type(label)
            elif label == 'O':
                if elem_start != -1:
                    if not elem_type in discard_types:
                        elems.add((elem_start, i, elem_type))
                elem_start = -1
                elem_type = None
    return elems

if len(argv) != 2:
    stderr.write('%s tagged_file\n' % argv[0])
    exit(1)

data = open(argv[1]).read().split('\n')

sys_data = []
gold_data = []

for line in data:
    if line == '':
        sys_data.append(('',''))
        gold_data.append(('',''))
    else:
        wf, gold_label, sys_label = line.split('\t')
        sys_data.append((wf, sys_label))
        gold_data.append((wf, gold_label))

sys_elems = get_elements(sys_data)
gold_elems = get_elements(gold_data)

sys_found_counts = ddict(lambda : 0.0)
gold_found_counts = ddict(lambda : 0.0)
sys_counts = ddict(lambda : 0.0)
gold_counts = ddict(lambda : 0.0)
sys_found_count = 0.0
gold_found_count = 0.0
sys_count = 0
gold_count = 0
for elem in sys_elems:
    if elem in gold_elems:
        sys_found_counts[elem[2]] += 1
        sys_found_count += 1
    sys_counts[elem[2]] += 1
    sys_count += 1

for elem in gold_elems:
    if elem in sys_elems:
        gold_found_counts[elem[2]] += 1
        gold_found_count += 1
    gold_counts[elem[2]] += 1
    gold_count += 1
print('\\documentclass{article}')
print('\\begin{document}')
print('\\begin{tabular}{l|ccc}')
print(' Type & Precision & Recall & F1\\\\')
print('\\hline')
for type in sys_found_counts:
    recall = 100*gold_found_counts[type] / gold_counts[type]
    precision = 100*sys_found_counts[type] / sys_counts[type]
    f = 2 * precision * recall / (precision + recall)
    print('%s &  %.2f & %.2f & %.2f\\\\' % (type.title(), precision, recall, f))

recall = 100*gold_found_count / gold_count
precision = 100*sys_found_count / sys_count
f = 2 * precision * recall / (precision + recall)
print('\\hline')
print('%s & %.2f & %.2f & %.2f' % ('ALL', precision, recall, f))
print('\\end{tabular}')
print()

confusions = ddict(lambda : ddict(lambda : 0.0))

for i, e in enumerate(gold_data):
    wf_gold, label_gold = e
    wf_sys, label_sys = sys_data[i]

    assert(wf_gold == wf_sys)
    if wf_gold == '':
        continue
    if (get_elem_type(label_gold) in discard_types or 
        get_elem_type(label_sys) in discard_types):
        continue
    confusions[label_gold][label_sys] += 1

tots = {l : sum(confusions[l].values()) for l in confusions}

print('\\begin{tabular}{l|%s}' % ('c' * len(confusions)))
print(' & %s\\\\' % ' & '.join([t.title() for t in sorted(confusions.keys())]))
print('\\hline')

for gold_label in sorted(confusions.keys()):
    stdout.write('%s & ' % gold_label.title())
    for i, sys_label in enumerate(sorted(confusions.keys())):
        stdout.write('%.2f %s' % (100 * confusions[gold_label][sys_label]/tots[gold_label], 
                                  '' if i + 1 == len(confusions) else ' & '))
    stdout.write('\\\\\n')
print('\\end{tabular}')
print('\\end{document}')
