import os, re
from python.amr import *
from python.txt import *
from python.ccg import *
import sys


CLASSES = {'0':TXT, '1':CCG}

name, html_file, amr_file, sent_file, classnum, BREAK_INTO_PARTS = sys.argv[1:]
template_file = 'template.html'
START, END = 0, 0
BREAK_INTO_PARTS = (BREAK_INTO_PARTS=='True')

cl = CLASSES[classnum]

def main():
    amrs = []
    sentences = []

    # AMRs
    with open(amr_file, 'r', encoding='utf8') as f:
        for amr in AMR.finditer(f.read()):
            amr = AMR(amr, 1)
            amrs.append(amr.html())
    # Sentences
    with open(sent_file, 'r', encoding='utf8') as f:
        for sent in cl.finditer(f.read()):
            sent = cl(sent)
            sentences.append(sent.html())
    # template
    html = ''
    with open(template_file, 'r', encoding='utf8') as f:
        html = f.read()
    # output
    content = []
    sent_amrs = [x for x in zip(sentences, amrs)]
    if BREAK_INTO_PARTS:
        sent_amrs = sent_amrs[START-1:END]
    i = START if BREAK_INTO_PARTS else 1
    for s, a in sent_amrs:
        content.append(
            f"""
<div amr-id ="{i}" class="aligner">
<h1>{i}. </h1><input  amr-id ="{i}" type="text" class="cmdline"/>
<button amr-id ="{i}" class="align">Add Alignment</button>
<div amr-id ="{i}" class="btn-group"></div><br/>
<anything amr-id ="{i}" class="{name}">{s}</anything>
<amr amr-id ="{i}">{a}</amr>
</div>""")
        i += 1

    content = ''.join(content)
    html = html.replace('{}', content).replace('{NAME}',name)
    with open(html_file, 'w', encoding='utf8') as f:
        f.write(html)


if __name__=="__main__":
    if BREAK_INTO_PARTS:
        h = html_file
        for i in range(4):
            START = i*50+1
            END = 50+START-1
            if BREAK_INTO_PARTS:
                html_file = h.replace('.html', f'_{START}-{END}.html')
            main()
    else:
        main()
