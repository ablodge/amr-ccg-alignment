import os, re
from utils.ccg import *
from utils.amr import *

amrs = []
sentences = []

amr_file = r'data/aligned_amrs.txt'
sent_file = r'data/ccg.txt'
template_file = r'template.html'
html_file = r'demo_v2.html'

def main():
    # AMRs
    with open(amr_file, 'r', encoding='utf8') as f:
        for amr in AMR.finditer(f.read()):
            amr = AMR(amr, 1)
            amrs.append(amr.html())
    # Sentences
    with open(sent_file, 'r', encoding='utf8') as f:
        for sent in CCG_Lexical.finditer(f.read()):
            sent = CCG_Lexical(sent)
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
            <div id ="{i}" class="aligner">
            <h1>{i}. </h1><input type="text" class="{i}"></input>
            <button class="align {1}">Add Alignment</button>
            <div class="btn-group {i}"></div><br/>
            <sentence class="{i}">{s}</sentence>
            <amr class="{i}">{a}</amr>
            </div>
            """)
        i += 1

    content = ''.join(content)
    html = html.replace('{}', content).replace('demo.js', 'demo_v1.js')
    with open(html_file, 'w', encoding='utf8') as f:
        f.write(html)
if __name__ == "__main__":
    main()


