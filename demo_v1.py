import os, re
from utils.txt import *
from utils.amr import *

amrs = []
sentences = []

amr_file = r'data/aligned_amrs.txt'
sent_file = r'data/amr_sentences.txt'
template_file = r'template.html'
html_file = r'demo_v1.html'

def main():
    # AMRs
    with open(amr_file, 'r', encoding='utf8') as f:
        for amr in AMR.finditer(f.read()):
            amr = AMR(amr, 1)
            amrs.append(amr.html())
    # Sentences
    with open(sent_file, 'r', encoding='utf8') as f:
        for sent in TXT.finditer(f.read()):
            sent = TXT(sent)
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
            <h1>{i}. </h1><input  amr-id ="{i}" type="text"></input>
            <button amr-id ="{i}" class="align">Add Alignment</button>
            <div amr-id ="{i}" class="btn-group"></div><br/>
            <sentence amr-id ="{i}">{s}</sentence>
            <amr amr-id ="{i}">{a}</amr>
            </div>
            """)
        i += 1

    content = ''.join(content)
    html = html.replace('{}', content).replace('demo.js', 'demo_v1.js')
    with open(html_file, 'w', encoding='utf8') as f:
        f.write(html)
if __name__ == "__main__":
    main()


