import os, re

amr_file = 'AMR_little_prince.txt'
md_file = 'AMR_little_prince.md'

AMR = ''
is_amr = False
md_output = ''

NODE_RE = re.compile('(?P<node>[a-z0-9]+)( )?/( )?(?P<concept>[a-z]+(-[0-9]+)?)')
EDGE_RE = re.compile(':[A-Za-z0-9-]+')

with open(amr_file, 'r', encoding='utf8') as f:
    for line in f:
        if line.startswith('101. '):
            break
        if re.match('^[(][a-z]', line):
            is_amr = True
            AMR += line
        elif is_amr and line.strip():
            AMR += line
        elif is_amr and not line.strip():
            is_amr = False
            finished = set()
            for node in NODE_RE.finditer(AMR):
                node = node.group()
                if not node in finished:
                    AMR = AMR.replace(node,'<font color="green">'+node+'</font>')
                    finished.add(node)
            for edge in EDGE_RE.finditer(AMR):
                edge = edge.group()
                if not edge in finished:
                    AMR = AMR.replace(edge,'<font color="blue">'+edge+'</font>')
                    finished.add(edge)
            md_output += "\n"+AMR+"\n"
            AMR.replace(' ','&nbsp;')
            AMR = ''
        else:
            md_output += line


with open(md_file, 'w', encoding='utf8') as f:
    f.write(md_output)