import os, re

amr_file = 'AMR_little_prince.txt'
md_file = 'AMR_little_prince.html'

AMR = ''
is_amr = False
md_output = ''

NODE_RE = re.compile('(?P<node>[a-z0-9]+)( )?/( )?(?P<concept>[a-z-]+([0-9]+)?)')
EDGE_RE = re.compile(':([A-Za-z0-9]|-)+(-of)?')

with open(amr_file, 'r', encoding='utf8') as f:
    for line in f:
        i = 0
        while line.startswith(' '):
            line = line.replace(' ', '', 1)
            i += 1
        line = ''.join('&nbsp;' for x in range(i))+line
        if re.match('^[(][a-z]', line):
            is_amr = True
            AMR += line
        elif is_amr and line.strip():
            AMR += line
        elif is_amr and not line.strip():
            is_amr = False
            # add AMR
            AMR = EDGE_RE.sub(repl=lambda edge: '<span style="color:blue">' + edge.group() + '</span>', string=AMR)
            AMR = NODE_RE.sub(repl=lambda node:'<span style="color:green">'+node.group()+'</span>', string=AMR)
            AMR = AMR.replace('\n', '<br />\n')
            md_output += "<br />\n"+AMR+"<br />\n"
            AMR = ''
        else:
            md_output += line


with open(md_file, 'w', encoding='utf8') as f:
    f.write(md_output)