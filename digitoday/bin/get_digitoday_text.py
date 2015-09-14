from sys import stdin, stderr
from html2text import html2text as h2t
from re import sub
from libhfst import load_pmatch
 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def remove_links(stx):
    return sub(r'\[([^\]]*)\]\([^\)]*\)', r'\1', stx)

def remove_emph(stx):
    stx = sub(r'_([^_]*)_',r'\1', stx)
    stx = sub(r'\*\*([^*]*)\*\*',r'\1', stx)
    return stx

def unstx(stx):
    return remove_emph(remove_links(stx))

def tokenize(txt, tokenizer, mark_p):
    paragraphs = str(txt).split('<>')
    paragraphs = [tokenizer.match(p) for p in paragraphs]
    tok_paragraphs = []

    for p in paragraphs:
        p = sub(r'[ \n\t\r]*<token>[ \t\n\r]*',r'<token>', p)
        p = sub(r'[ \n\t\r]*</token>[ \t\n\r]*',r'</token>', p)
        p = sub(r'(<token>[.!?]</token>)<',r'\1<SENTENCE><', p)
        p = sub(r'<[/]*token>',r'\n', p)
        p = sub(r'[\n]+',r' ', p)
        p = sub(r'[ \n]+',r'\n', p)
        p = p.replace('<SENTENCE>','')
        p = sub(r'^[ \t\n\r]*',r'',p)
        p = sub(r'[ \t\n\r]*$',r'',p)
        if p != '':
            tok_paragraphs.append(p)

    if mark_p:
        return '<PARAGRAPH>\n' + '\n\n<PARAGRAPH>\n'.join(tok_paragraphs)
    else:
        return '\n\n'.join(tok_paragraphs)
recording = 0

data = ''

tokenizer = load_pmatch('../omorfi/tokenize.hfst')
   
for line in stdin:
    line = line.strip()
    if line.find('<!-- ISI_LISTEN_START -->') != -1:
        recording = 1
    elif line.find('<!-- ISI_LISTEN_STOP -->') != -1:
        recording = 0
    elif line.find('<div class="storyTools vertical ISI_IGNORE') != -1:
        recording = 2
    elif recording == 2 and line.find('</div>') != -1:
        recording = 1
    else:
        if recording == 1:
            data += line

title_start = data.find('<h1')
data = data[title_start:]
title_stop  = data.find('</h1>')
title = h2t(data[:title_stop])
data = data[title_stop:]

date_start = data.find('<p class="ingress"><span class="date">')
data = data[date_start:]
date_stop = data.find('</span>')
date = h2t(data[:date_stop])
data = data[date_stop:]

ingress_stop = data.find('</p>')
ingress = h2t(data[:ingress_stop])
data = data[ingress_stop:]

body_start = data.find('<p')
data = data[body_start:]
body_stop = data.rfind('</p>')
body = h2t(data[:body_stop])

title = unstx(title.replace('#','').replace('\n',''))
title = tokenize(title, tokenizer, 0)
print('<HEADLINE>')
print(title)
print('')

date = unstx(date.replace('\n',''))
print('<DATE>')
print(date.replace('\n',''))
print('')

ingress = unstx(ingress.replace('\n',' '))
ingress = tokenize(ingress, tokenizer, 0)
print('<INGRESS>')
print(ingress)
print('')

body = unstx(body.replace('\n\n','<>').replace('\n',' '))
body = tokenize(body, tokenizer, 1)
print('<BODY>')
print(body)

