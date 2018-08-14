import os, re

amr_file = 'AMR_little_prince.txt'
md_file = 'AMR_little_prince.md'

AMR = ''
is_amr = False
md_output = ''

with open(amr_file, 'r', encoding='utf8') as f:
    for line in f:
        if re.match('^[(][a-z]', line):
            is_amr = True
            AMR += line
        elif is_amr and line.strip():
            AMR += line
        elif is_amr and not line.strip():
            is_amr = False
            md_output += "```\n"+AMR+"```\n"
            AMR = ''
        else:
            md_output += line


with open(md_file, 'w', encoding='utf8') as f:
    f.write(md_output)