import re, os
os.chdir(r'C:\Users\austi\Desktop\AMR-CCG\data')

SNT_RE = re.compile('# ::snt (.*?)\s*\n\s*')

file = 'aligned_amrs.txt'
output_file = 'amr_sentences.txt'

snts = []

with open(file, 'r', encoding='utf8') as f:
    for line in f:
        if SNT_RE.match(line):
            snts.append(SNT_RE.match(line).group(1))

with open(output_file, 'w', encoding='utf8') as f:
    for sent in snts:
        f.write(sent+'\n\n')
