import os, re

amr_file = 'AMR_little_prince.txt'
md_file = 'AMR_little_prince.html'

AMR = ''
is_amr = False
md_output = ''

NODE_RE = re.compile('(?P<node>[a-z0-9]+)( )?/( )?(?P<concept>[a-z]+(-[0-9]+)?)')
EDGE_RE = re.compile(':[A-Za-z0-9-]+')

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
            finished = set()
            # add AMR
            TMP_AMR = AMR
            for node in NODE_RE.finditer(TMP_AMR):
                node = node.group()
                if not node in finished:
                    AMR = AMR.replace(node,'<span style="color:green"><i>'+node+'</i></span>')
                    finished.add(node)
            for edge in EDGE_RE.finditer(TMP_AMR):
                edge = edge.group()
                if not edge in finished:
                    AMR = AMR.replace(edge,'<span style="color:blue"><b>'+edge+'</b></span>')
                    finished.add(edge)
            AMR = AMR.replace('\n', '<br />\n')
            md_output += "\n"+AMR+"\n\n"
            AMR = ''
        else:
            md_output += line


with open(md_file, 'w', encoding='utf8') as f:
    f.write(md_output)