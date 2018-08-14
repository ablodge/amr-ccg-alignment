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
        if re.match('^[(][a-z]', line):
            is_amr = True
            AMR += line
        elif is_amr and line.strip():
            AMR += line
        elif is_amr and not line.strip():
            is_amr = False
            for node in NODE_RE.finditer(AMR):
                AMR = AMR.replace(node.group(),'<font color="green">'+node.group()+'</font>',1)
            for edge in EDGE_RE.finditer(AMR):
                AMR = AMR.replace(edge.group(),'<font color="blue">'+edge.group()+'</font>',1)

            md_output += "```\n"+AMR+"```\n"
            AMR = ''
        else:
            md_output += line


with open(md_file, 'w', encoding='utf8') as f:
    f.write(md_output)