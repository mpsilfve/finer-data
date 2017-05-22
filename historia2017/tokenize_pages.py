# -*- coding: utf-8 -*-

import sys
#import os.path
import os
import random
import csv
import re

reload(sys)
sys.setdefaultencoding('UTF-8')


# stop lists

stop_list_abbv_names = ['Alb.', 'Konst.', 'And.', 'Matinp.', 'Juosepinp.', 'Rich.', 'Berl.', 'Em.', 'Vict.', 'Pert.', 'Ferd.', 'Edw', 'And.', 'Gabr.', 'Edw.', 'Didr.', 'Jon.', 'Koloss.', 'Lut.', 'Erikinp.', 'Ont.', 'Jes.', 'Hebr.', 'Hepr.', 'Kol.', 'Matth.', 'Es.', 'Alfr.', 'Job.', 'Ap.', 'Luk.', 'Tim.', 'Rom.', 'Mark.', 'Math.', 'Es.', 'Kun.', 'Luuk.', 'Moos.', 'Mos.', 'Tess.', 'Kor.', 'Hab.', 'Piet.', 'Wilh.', 'Joh.', 'Walfr.', 'Kris.', 'Magn.', 'Fr.', 'Pr.', 'Andr.', 'Gust.', 'Art.', 'Ad.', 'Th.', 'Chr.', 'Ch.', 'Fredr.', 'Wibl.', 'Hbl.', 'Konr.', 'Aug.', 'Wald.', 'Rob.', 'Leon.', 'Kust.', 'Reinh.', 'Piet.', 'Tulliporttik.', 'Zach.', 'Reinh.', 'Alex.', 'Ludw.', 'Walt.', 'Wilhelminp.']
stop_list_months = ['tammik.', 'helmik.', 'maalisk.', 'huhtik.', 'toukok.', 'kesäk.', 'heinäk.', 'elok.', 'syysk.', 'lokak.', 'marrask.', 'jouluk.', 'Tammik.', 'Helmik.', 'Maalisk.', 'Huhtik.', 'Toukok.', 'Kesäk.', 'Heinäk.', 'Elok.', 'Syysk.', 'Lokak.', 'Marrask.', 'Jouluk.']
stop_list_abbvs_lc = ['lautam.', 'raittiusyhd.', 'kolm.', 'ed.', 'wp.', 'wuot.', 'ed.', 'alam.', 'hiippak.', 'wuosik.', 'ruokalus.', 'pyh.', 'heng.', 'rpl.', 'row.', 'sunnunt.', 'ewank.', 'yliop.', 'ps.', 'smk.', 'luth.', 'ev.', 'wk.', 'engl.', 'kansak.', 'mn.', 'gr.', 'toim.', 'os.', 'kysym.', 'esim.', 'y.m.', 'siw.', 'riw.', 'ylh.', 'aam.', 'jpp.', 'epp.', 'kirkkoh.', 'kirkk.', 'prof.', 'j.p.p.', 'e.p.p.', 'päiw.', 'ilm.', 'min.', 't.p.p.', 'keis.', 'milj.', 'kortt.', 'kaup.os.', 'tynn.', 'jatk.', 'pp.', 'wapaah.', 'kirurg.', 'toht.', 'mk.', 'j.pp.', 'mark.', 'mp.', 'np.', 'op.', 'mbl.', 'postik.', 'e.pp.', 'j.pp.', 'huom.', 'kapp.', 'lle.pp.', 'joh.', 'kumpp.', 'edust.', 'litr.', 'hehtol.', 'tuomiok.', 'kappal.', 'pit.', 'apul.', 'yliopp.', 'tim.', 'eph.', 'cph.', 'ilm.', 'thess.', 'kor.', 'mos.', 'ew.', 'math.', 'semin.', 'tn.', 'wakin.', 'opett.', 'wak.', 'leht.', 'mkk.', 'wuod.', 'kuuk.', 'apl.', 'disk.', 'kunk.', 'ylössanomis.', 'maksettaw.', 'inb.', 'uppl.', 'hj.', 'p.p.', 'kirj.', 'ham.', 'san.', 'pohjal.', 'kihlak.', 'kirj.', 'no.', 'st.', 'co.', 'lähet.', 'nim.', 'ent.', 'jatket.', 'y.m.', 'doll.', 'cent.', 'neidet.', 'maist.', 'kirjakaupp.', 'leht.', 'yht.', 'mpl.', 'npl.', 'eläw.', 'taloneläkem.', 'ruotuwaiw.', 'miesp.', 'naisp.', 'mrk.', 'st.', 'kand.', 'suom.', 'pohj.', 'maanw.', 'howioik.', 'asess.', 'lakit.', 'nimit.', 'vr.', 'abl.', 'arm.', 'häml.', 'häm.', 'nimikirkkoh.', 'kirkh.', 'w.kirkh.', 'room.', 'rupl.', 'kop.', 'w.t.', 'n.kirkh.', 'wapah.', 'erinom.', 'warapuheenj.', 'aamul.', 'metr.', 'pen.', 'lääket.', 'ål.', 'tuh.', 'minn.', 'mosk.', 'jyr.', 'arw.', 'toimit.', 'esm.', 'wara-kirkkoh.', 'kunn.', 'esqr.', 'handl.', 'ruohonp.', 'kl.', 'kump.', 'wirst.', 'jälk.', 'markk.', 'in.', 'fk.', 'lääk.', 'lisent.', 'sisäänt.', 'ulosm.', 'kuutmetr.', 'regton.', 'tuutmetr.', 'sylt.', 'wanh.', 'hn.', 'sam.', 'kg.', 'sentim.', 'kaupp.', 'suomal.', 'luth.', 'länsis.', 'suoment.', 'fil.', 'filos.', 'historiallis-kielit.', 'fys.', 'matst.', 'uusm.', 'kapt.', 'ins.', 'finl.', 'nimitt.', 'n.s.', 'kyyn.', 'tuum.', 'kynn.', 'hop.', 'synt.', 'wirsik.', 'päiv.', 'lähetysruk.', 'ruots.', 'past.', 'ruotsal.', 'insin.', 'kaup.', 'prosent.', 'satak.', 'helm.', 'ensim.', 'kaikk.', 'leiw.', 'palw.', 'seurak.', 'ruotuw.', 'työmieh.', 'palwelust.', 'mol.', 'läks.', 'tyt.', 'talollisent.', 'kr.', 'mr.', 'waraesim.', 'tiet.', 'postim.', 'kpl.', 'kp.', 'myyj.', 'ostaj.', 'rpl.', 'string.', 'franc.', 'mrt.', 'gld.', 'sat.', 'laat.', 'taloll.', 'knr.',' kgr.', 'puolip.', 'prow.', 'pormest.', 'porm.']
#stop_list_abbvs_uc = []
#for abbv in stop_list_abbvs_lc:
#    abbv = abbv[0].upper() + abbv[1:]
#    stop_list_abbvs_uc.append(abbv)
stop_list_misc = ['..', '...', '....']
            
# loop files in directory sys.argv[1]

files = [f for f in os.listdir(sys.argv[1] + '/') if os.path.isfile(os.path.join(sys.argv[1] + '/', f))]

for file_in in files:

    if file_in[len(file_in)-4:] != '.csv':
        continue

    # read raw page in
    data_in = list(csv.reader(open(sys.argv[1] + '/' + file_in, 'rb'), delimiter='\t', quotechar='', quoting=csv.QUOTE_NONE, escapechar=''))
    word_index = int(sys.argv[3]) # which column to tokenize
    
    data_out = []
    for line in data_in:
        
        line.insert(word_index+1, line[word_index]) # this column will be tokenized
        line.insert(word_index+2, '') # create empty column for annotation
        data_out.append(line)

    line_out = []
    for elem in line:
        line_out.append('')
    line_out[0] = '<tokenized>'
    data_out.append(line_out)

    data_in = data_out
        
    modified = True

    while(modified):
    
        data_out = []

        for line_index in range(0, len(data_in)):

            line_in = data_in[line_index]
            word = line_in[word_index+1]

            if line_index != len(data_in)-1:
                next_line_in = data_in[line_index+1]
                next_word = next_line_in[word_index+1]
            else:
                next_word = ''
                
            if word == '':

                data_out.append(line_in)
                
            elif len(word) == 1:

                data_out.append(line_in)

            elif word[0] in ['(', '"', ',', '\'', '?']:

                line_out = []
                for elem in line_in:
                    line_out.append('')
                line_out[0] = '<tokenized>'
                line_out[word_index+1] = word[0]
                data_out.append(line_out)
                
                line_in[word_index+1] = word[1:]
                data_out.append(line_in)

            elif word[-1] in [',', ';', '*']: # if word ends in '-' or '\'', leave it be

                line_in[word_index+1] = word[:len(word)-1]
                data_out.append(line_in)

                line_out = []
                for elem in line_in:
                    line_out.append('')
                line_out[0] = '<tokenized>'
                line_out[word_index+1] = word[-1]
                data_out.append(line_out)

            elif word[-1] in ['.', '?', '!', ':'] and \
            word.lower() not in stop_list_abbvs_lc and \
            word not in stop_list_months and \
            word not in stop_list_abbv_names and \
            word not in stop_list_misc and \
            re.match('^[0-9]\.$', word) == None and \
            re.match('^([a-z]|ä|ö|å)\.$', word) == None and \
            re.match('^([A-Z]|Ä|Ö|Å)\.$', word) == None and \
            re.match('^([a-z]|ä|ö|å)\.([a-z]|ä|ö|å)\.$', word) == None and \
            re.match('^([A-Z]|Ä|Ö|Å)\.([A-Z]|Ä|Ö|Å)\.$', word) == None and \
            re.match('^([A-Z]|Ä|Ö|Å)\.\-([A-Z]|Ä|Ö|Å)\.$', word) == None:

                line_in[word_index+1] = word[:len(word)-1]
                data_out.append(line_in)

                line_out = []
                for elem in line_in:
                    line_out.append('')
                line_out[0] = '<tokenized>'
                line_out[word_index+1] = word[-1]
                data_out.append(line_out)

                line_out = []
                for elem in line_in:
                    line_out.append('')
                line_out[0] = '<tokenized>'
                line_out[word_index+1] = ''
                data_out.append(line_out)

            elif word[-1] in [')', '"']:

                line_in[word_index+1] = word[:len(word)-1]
                data_out.append(line_in)

                line_out = []
                for elem in line_in:
                    line_out.append('')
                line_out[0] = '<tokenized>'
                line_out[word_index+1] = word[-1]
                data_out.append(line_out)
                
            else:
                
                data_out.append(line_in)

#        print len(data_in), len(data_out)

        if len(data_in) != len(data_out):
                
            data_in = data_out
            modified = True
            
        else:               

            modified = False

#        print modified
        
    # remove extra empty lines due to tokenization

    remove_indexes = []
    for i in range(1, len(data_out)):
        
        prev_line = data_out[i-1]
        this_line = data_out[i]
        
        if prev_line[0] == '<tokenized>' and this_line[0] == '<tokenized>':

            if prev_line[word_index+1] == '' and this_line[word_index+1] == ')': # continue here
                remove_indexes.append(i-1)
 
            if prev_line[word_index+1] == '' and this_line[word_index+1] == '':
                remove_indexes.append(i)

    for i in reversed(remove_indexes):
        
        del data_out[i]
            
            
    FILE = open(sys.argv[2] + '/' + file_in, 'w')
    csvwriter = csv.writer(FILE, delimiter='\t', quotechar='', quoting=csv.QUOTE_NONE, escapechar='')
    for line in data_out:
        csvwriter.writerow(line)
    FILE.close()


