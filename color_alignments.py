import os, re

amr_file = 'amr.txt'
html_file = 'amr.html'
align_file = 'amr_ud_align.txt'




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
    NODE_RE = re.compile('([a-z][0-9]*|none[0-9]+)( ?/ ?[A-Za-z-]+[0-9]*)')
    EDGE_RE = re.compile('(:([A-Za-z0-9]|-)+(-of)?)')
    amr = None
    amr_split = None
    structure = None
    nodes = None
    edges = None
    edge_from_index = None
    sentence = ''

    colors = None

    def __init__(self, string, sentence):
        self.sentence = sentence
        self.amr = string.replace('&nbsp;',' ')
        self.amr_split = [x[0] for x in re.findall('('+self.NODE_RE.pattern + '|' + self.EDGE_RE.pattern + '|' + '[()]' + '|[^\s()]+|\s+)', self.amr)]
        self.structure = [x[0] for x in re.findall('('+self.NODE_RE.pattern + '|' + self.EDGE_RE.pattern + '|' + '[()]' + '|[^\s()]+)', self.amr)]
        self.nodes = [x.replace(' ','') for i, x in enumerate(self.structure) if self.NODE_RE.match(x)]
        self.edges = []
        self.edge_from_index = {}
        self.colors = {}

        depth = -1
        parents = []
        last_node = None
        for i, x in enumerate(self.amr_split):
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
                for j in range(i+1, len(self.amr_split)):
                    next = self.amr_split[j]
                    if not next.strip(): continue
                    if next=='(': continue
                    if next==')': break
                    if self.EDGE_RE.match(next): break
                    trg = ' '+self.normalize_node(next)
                self.edges.append(src+x+trg)
                self.edge_from_index[i] = src+x+trg


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
            key = self.normalize_node(x)
            if i in self.edge_from_index:
                key = self.edge_from_index[i]
            if key in self.colors:
                split[i] = '<span class="'+self.colors[key]+'">'+ x + '</span>'
        return ' '.join(sentence)+'<br />\n'+''.join(split)

    def assign_node_color(self, node, color):
        self.colors[self.normalize_node(node)] = color

    def assign_edge_color(self, edge, color):
        self.colors[edge] = color

    def assign_word_color(self, index, color):
        self.colors[str(index)] = color

    def normalize_node(cls, node):
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
        self.amr_struct = []
        self.ud_lex = {}
        self.ud_struct = []
        self.sent_lex = {}
        self.sent_struct = []

        for index, line in enumerate(string.split('\n')):
            if not '    #    ' in line:
                continue
            split = line.split('    #    ')
            amr_align = split[0]
            amr_align = re.sub('none[0-9]+/','',amr_align)
            ud_align = split[1]
            # lexical alignment
            if not ' ' in amr_align and not ' ' in ud_align:
                if amr_align in self.amr_lex:
                    index = self.amr_lex[amr_align]
                if ud_align in self.ud_lex:
                    index = self.ud_lex[ud_align]
                self.amr_lex[amr_align] = index
                self.ud_lex[ud_align] = index
                self.sent_lex[ud_align.split('/')[0]] = index
                print(line)
                print(self.amr_lex, self.ud_lex)
            # structural alignment
            else:
                # split amr align into edges and nodes
                align_split = [x[0] for x in re.findall('('+AMR_Structure.NODE_RE.pattern+'|'+AMR_Structure.EDGE_RE.pattern+'|[^\s|()]+)', amr_align)]
                node_list = []
                for i, x in enumerate(align_split):
                    if AMR_Structure.NODE_RE.match(x):
                        node_list.append(x)
                    if not AMR_Structure.EDGE_RE.match(x):
                        node = x
                        self.amr_struct.append((node, index))
                    if AMR_Structure.EDGE_RE.match(x):
                        edge = None
                        if len(align_split)>i+1 and not AMR_Structure.EDGE_RE.match(align_split[i+1]):
                            edge = x+' '+align_split[i+1].split('/')[0].strip()
                        else:
                            edge = x
                        for node in node_list:
                            e = node.split('/')[0].strip()+' '+edge
                            self.amr_struct.append((e, index))
                # split ud align into edges and nodes
                ud_split = [x for x in re.findall('(' + self.UD_NODE_RE.pattern + '|' + self.UD_EDGE_RE.pattern + '|[^\s|()]+)',ud_align)]
                for i, x in enumerate(ud_split):
                    if self.UD_NODE_RE.match(x):
                        self.ud_struct.append((x, index))
                        self.sent_struct.append((x.split('/')[0], index))
                print(line)
                print(self.amr_struct, self.ud_struct)


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
                align = ALIGN[sentence]
                # add AMR
                # lexical alignments
                html_output += "Lexical Alignments:<br />\n"
                amr = AMR_Structure(AMR, sentence)
                for node in align.amr_lex:
                    amr.assign_node_color(node, get_color(align.amr_lex[node]))
                for word in align.sent_lex:
                    amr.assign_word_color(int(word)-1, get_color(align.sent_lex[word]))
                html_output += "<br />\n"+str(amr)+"<br />\n"
                # structural alignments
                index = 1
                for i in set([i for x,i in align.amr_struct]):
                    html_output += "Structural Alignments "+str(index)+":<br />\n"
                    html_output += str([x for x,j in align.amr_struct if j==i])+"<br />\n"
                    amr = AMR_Structure(AMR, sentence)
                    for x,j in align.amr_struct:
                        if j==i:
                            if not ' ' in x:
                                amr.assign_node_color(x, get_color(i))
                            else:
                                amr.assign_edge_color(x, get_color(i))
                    for word,j in align.sent_struct:
                        if j == i:
                            amr.assign_word_color(int(word) - 1, get_color(i))
                    html_output += "<br />\n" + str(amr) + "<br />\n"
                    index += 1
            AMR = ''


with open(html_file, 'w', encoding='utf8') as f:
    f.write(html_start+html_output+html_end)