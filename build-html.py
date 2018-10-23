import os, re
from python.amr import *
from python.txt import *
from python.ccg import *
import sys


CLASSES = {'0':TXT, '1':CCG}

name, html_file, amr_file, sent_file, classnum = sys.argv[1:]
template_file = 'template.html'



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
    i = 1
    for s, a in zip(sentences, amrs):
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
    main()
