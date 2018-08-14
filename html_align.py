import os, re

amr_file = 'AMR_little_prince.txt'
html_file = 'AMR_little_prince.html'
align_file = 'AMR_UD_little_prince.txt'




AMR = ''
is_amr = False
html_output = ''
html_start = '''
<!DOCTYPE html>
<html>
<head>
<style>
.grey { text-decoration: none; background-color: #eee; }
.red { text-decoration: none; background-color: #f5b7b1; }
.orange { text-decoration: none; background-color: #f5cba7; }
.yellow { text-decoration: none; background-color: #f9e79f; }
.green { text-decoration: none; background-color: #abebc6; }
.blue { text-decoration: none; background-color: #aed6f1; }
.purple { text-decoration: none; background-color: #d7bde2; }
.black { text-decoration: none; background-color: #566573; }
.none { }
</style>
</head>
<body>
'''
html_end = '''
</body>
</html> 
'''




class AMR_Structure:
    NODE_RE = re.compile('[a-z0-9-]+(( )?/( )?[a-z-]+([0-9]+)?)?')
    EDGE_RE = re.compile(':([A-Za-z0-9]|-)+(-of)?')
    amr = None
    structure = None
    nodes = None
    edges = None

    def __init__(self, string):
        self.amr = string.replace('&nbsp;',' ')
        self.nodes = [x for x in self.NODE_RE.findall(self.amr)]
        self.edges = []

        depth = 0
        self.structure = [x[0] for x in re.findall('('+self.NODE_RE.pattern+'|'+self.EDGE_RE.pattern+'|'+'[()])', self.amr)]
        print(self.nodes)




class UD_Structure:
    ...


AMR_ALIGN = {}
UD_ALIGN = {}

with open(align_file, 'r', encoding='utf8') as f:
    sentence = ''
    for line in f:
        if re.match('^# ::snt ',line):
            sentence = line[len('# ::snt '):].strip()
            AMR_ALIGN[sentence] = []
            UD_ALIGN[sentence] = []
        elif '    #    ' in line:
            align = line.split('    #    ')

            if not ' ' in align[0]:
                AMR_ALIGN[sentence].append(align[0])
                UD_ALIGN[sentence].append(align[1])
            else:
                continue
COLORS = {0:'blue',1:'green',2:'purple',3:'red',4:'yellow',5:'orange',6:'grey',7:'black'}

def get_color(match, snt):
    s = match.group().replace(' ', '')
    index = None
    if not snt in AMR_ALIGN:
        return 'none'
    for j, align in enumerate(AMR_ALIGN[snt]):
        if align in s:
            index = j
            break
    if index:
        return COLORS[index % len(COLORS)]
    else:
        return 'none'

with open(amr_file, 'r', encoding='utf8') as f:
    sentence = ''
    for line in f:
        i = 0
        while line.startswith(' '):
            line = line.replace(' ', '', 1)
            i += 1
        line = ''.join('&nbsp;' for x in range(i))+line
        x = re.match('^[0-9]+[.] (?P<snt>.*) [(]lpp_1943[.][0-9]+[)]', line)
        if x:
            sentence = x.group('snt')
            if sentence in UD_ALIGN:
                words = line.strip().split()
                for i, word in enumerate(words):
                    for j, align in enumerate(UD_ALIGN[sentence]):
                        if ' '+str(i)+'/' in ' '+align:
                            words[i] = '<span class="'+COLORS[j%len(COLORS)]+'">'+str(i)+'/' + word + '</span>'
                line = ' '.join(words)
                html_output += line.replace('\n','<br />\n')
        elif re.match('^[(][a-z]', line):
            is_amr = True
            AMR += line
        elif is_amr and line.strip():
            AMR += line
        elif is_amr and not line.strip():
            is_amr = False
            # add AMR
            AMR_Structure(AMR)
            AMR = AMR_Structure.EDGE_RE.sub(repl=lambda edge: '<span class="'+get_color(edge,sentence)+'">' + edge.group() + '</span>', string=AMR)
            AMR = AMR_Structure.NODE_RE.sub(repl=lambda node:'<span class="'+get_color(node,sentence)+'">'+node.group()+'</span>', string=AMR)
            AMR = AMR.replace('\n', '<br />\n')
            if sentence in AMR_ALIGN:
                html_output += "<br />\n"+AMR+"<br />\n"
            AMR = ''
        else:
            html_output += line


with open(html_file, 'w', encoding='utf8') as f:
    f.write(html_start+html_output+html_end)