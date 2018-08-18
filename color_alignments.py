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
    NODE_RE = re.compile('[a-z][0-9]*( ?/ ?[A-Za-z-]+[0-9]*)')
    EDGE_RE = re.compile('(:([A-Za-z0-9]|-)+(-of)?)')
    amr = None
    amr_split = None
    structure = None
    nodes = None
    edges = None
    sentence = ''

    colors = None

    def __init__(self, string, sentence):
        self.sentence = sentence
        self.amr = string.replace('&nbsp;',' ')
        self.amr_split = [x[0] for x in re.findall('('+self.NODE_RE.pattern + '|' + self.EDGE_RE.pattern + '|' + '[()]' + '|[^\s()]+|\s+)', self.amr)]
        self.structure = [x[0] for x in re.findall('('+self.NODE_RE.pattern + '|' + self.EDGE_RE.pattern + '|' + '[()]' + '|[^\s()]+)', self.amr)]
        self.nodes = [x.replace(' ','') for i, x in enumerate(self.structure) if self.NODE_RE.match(x)]
        self.edges = []
        self.edge_indices = []
        self.colors = {}

        depth = -1
        parents = []
        last_node = None
        for i, x in enumerate(self.structure):
            if x=='(':
                depth+=1
                parents.append(last_node)
            elif x==')':
                depth-=1
                parents.pop()
            if self.NODE_RE.match(x):
                last_node = x
                parents[depth] = x
            if self.EDGE_RE.match(x):
                src = self.normalize_node(parents[-1])+' '
                trg = ''
                if len(self.structure)>i+1:
                    y = self.structure[i+1]
                    if not y=='(' and not self.EDGE_RE.match(y):
                        trg = ' '+self.normalize_node(y)
                if len(self.structure)>i+2:
                    z = self.structure[i+2]
                    if y=='(' and not z=='(' and not self.EDGE_RE.match(z):
                        trg = ' '+self.normalize_node(z)
                self.edges.append(src+x+trg)
        print(self.edges)
        print(self.nodes)

    def __str__(self):
        # sentence
        sentence = self.sentence.split()
        for i, x in enumerate(sentence):
            if str(i) in self.colors:
                sentence[i] = '<span class="'+self.colors[str(i)]+'">'+ x + '</span>'
        # amr
        split = self.amr_split
        # make line breaks html safe (<br />)
        split = [x.replace('\n','<br />\n') for x in split]
        # make leading spaces html safe (&nbsp;)
        for i,x in enumerate(split):
            if '\n' in x:
                split[i] = x[:x.index('\n')] + x[x.index('\n'):].replace(' ', '&nbsp;')
        # convert nodes and edges to the right color
        for i, x in enumerate(split):
            key = x.split('/')[0].strip()
            if key in self.colors:
                split[i] = '<span class="'+self.colors[key]+'">'+ x + '</span>'
        return ' '.join(sentence)+'<br />\n'+''.join(split)

    def assign_node_color(self, node, color):
        self.colors[self.normalize_node(node)] = color

    def assign_edge_color(self, edge, color):
        self.colors[edge] = color

    def assign_word_color(self, index, color):
        self.colors[str(index)] = color

    def normalize_node(self, node):
        return node.split('/')[0].strip()


class UD_Structure:
    ud = None
    sentence = ''
    structure = None

    def __init__(self, string, sentence):
        self.ud = string
        self.sentence = sentence
        self.structure = [x.split() for x in string.split('\n')]

    def __str__(self):
        return self.ud

class AMR_UD_Alignment:
    NODE_RE = re.compile('([a-z][0-9]*|none[0-9]+)( ?/ ?[A-Za-z+-]+[0-9]*)?')
    EDGE_RE = re.compile('(:([A-Za-z0-9]|-)+(-of)?)')
    UD_NODE_RE = re.compile('[0-9]+/\S+')
    UD_EDGE_RE = re.compile(':\S+')

    amr_lex = {}
    amr_struct = {}
    ud_lex = {}
    ud_struct = {}
    sent_lex = {}
    sent_struct = {}

    def __init__(self, string):
        self.amr_lex = {}
        self.amr_struct = {}
        self.ud_lex = {}
        self.ud_struct = {}
        self.sent_lex = {}
        self.sent_struct = {}

        for i, line in enumerate(string.split('\n')):
            if not '    #    ' in line:
                continue
            split = line.split('    #    ')
            amr_align = split[0]
            amr_align = re.sub('none[0-9]+/','',amr_align)
            ud_align = split[1]
            # lexical alignment
            if not ' ' in amr_align and not ' ' in ud_align:
                if amr_align in self.amr_lex:
                    i = self.amr_lex[amr_align]
                if ud_align in self.ud_lex:
                    i = self.ud_lex[ud_align]
                self.amr_lex[amr_align] = i
                self.ud_lex[ud_align] = i
                self.sent_lex[ud_align.split('/')[0]] = i
            # structural alignment
            else:
                # split amr align into edges and nodes
                align_split = [x[0] for x in re.findall('('+self.NODE_RE.pattern+'|'+self.EDGE_RE.pattern+')', amr_align)]
                for i, x in enumerate(align_split):
                    if self.NODE_RE.match(x):
                        node = x
                        self.amr_struct[node] = i
                    elif self.EDGE_RE.match(x):
                        edge = None
                        if len(align_split)>i+1 and self.NODE_RE.match(align_split[i+1]):
                            edge = x+' '+align_split[i+1]
                        else:
                            edge = x
                        self.amr_struct[edge] = i
                # split ud align into edges and nodes
                self.ud_struct[ud_align] = i



def get_color(index):
    colors = {0:'blue',1:'green',2:'red',3:'purple',4:'grey',5:'yellow',6:'orange'}
    return colors[int(index)%7]

ALIGN = {}
with open(align_file, 'r', encoding='utf8') as f:
    sentence = ''
    align = ''
    for line in f:
        # sentence regex
        if re.match('^# ::snt ',line):
            sentence = line[len('# ::snt '):].strip()
        elif '    #    ' in line:
            align += line
        elif align and not line.strip():
            ALIGN[sentence] = AMR_UD_Alignment(align)
            align = ''

with open(amr_file, 'r', encoding='utf8') as f:
    sentence = ''
    for line in f:
        # sentence regex
        x = re.match('^[0-9]+[.] (?P<snt>.*) [(]lpp_1943[.][0-9]+[)]', line)
        if x:
            sentence = x.group('snt')
        elif re.match('^[(][a-z]', line):
            is_amr = True
            AMR += line
        elif is_amr and line.strip():
            AMR += line
        elif is_amr and not line.strip():
            is_amr = False
            if sentence in ALIGN:
                # add AMR
                amr = AMR_Structure(AMR, sentence)
                for node in ALIGN[sentence].amr_lex:
                    amr.assign_node_color(node, get_color(ALIGN[sentence].amr_lex[node]))
                for word in ALIGN[sentence].sent_lex:
                    amr.assign_word_color(int(word)-1, get_color(ALIGN[sentence].sent_lex[word]))
                html_output += "<br />\n"+str(amr)+"<br />\n"
            AMR = ''


with open(html_file, 'w', encoding='utf8') as f:
    f.write(html_start+html_output+html_end)