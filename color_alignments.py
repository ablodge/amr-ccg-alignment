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
<link rel="stylesheet" href="color_alignments.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="color_alignments.js"></script>
</head>
<body>
'''
html_end = '''
</body>
</html> 
'''
def html_elem(type, content, cls=None, id=None):
    cls = ' class="'+cls+'"' if cls else ''
    id = ' id="'+id+'"' if id else ''
    return '<'+type+cls+id+'>' + content + '</'+type+'>'


class AMR_Structure:
    NODE_RE = re.compile('([a-z][0-9]*|none[0-9]+)( ?/ ?[A-Za-z-]+[0-9]*)')
    EDGE_RE = re.compile('(:([A-Za-z0-9]|-)+(-of)?)')

    def __init__(self, string, sentence, id):
        self.id = id
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


    def html(self):
        sentence_id = str(self.id)
        # sentence
        words = self.sentence.split()
        for i, x in enumerate(words):
            if str(i) in self.colors:
                color_ids = ['tok-' + sentence_id + '-' + x for x in set(self.colors[str(i)])]
                words[i] = html_elem('span', x, cls=' '.join(['tok','tok-'+sentence_id]+color_ids))
        # amr
        amr_split = self.amr_split
        amr_split = [x.replace('\n','<br />\n') for x in amr_split]
        for i,x in enumerate(amr_split):
            if '\n' in x:
                amr_split[i] = x[:x.index('\n')] + x[x.index('\n'):].replace(' ', '&nbsp;')
        # convert nodes and edges to the right color
        buttons = []
        for i, x in enumerate(amr_split):
            key = self.normalize_node(x)
            if i in self.edge_from_index:
                key = self.edge_from_index[i]
            if key in self.colors:
                color_ids = ['tok-'+sentence_id+'-'+x for x in set(self.colors[key])]
                amr_split[i] = html_elem('span', x, cls=' '.join(['tok','tok-'+sentence_id]+color_ids))
                buttons += self.colors[key]
        sentence_html = html_elem('p', ' '.join([sentence_id+'.']+words), cls='sentence sentence-'+sentence_id, id=sentence_id) + '<br />\n'
        buttons_html = [html_elem('button', 'lexical' if 'lex' in b else 'structural', cls='button-'+sentence_id+'-'+b, id=str(i)) for i,b in enumerate(sorted(set(buttons)))]
        amr_html =      html_elem('p', ''.join(amr_split), cls='amr amr-'+sentence_id) + '<br />\n'
        return sentence_html +\
               '<div class="btn-group">'+''.join(buttons_html)+'</div><br />\n'+\
               amr_html

    def assign_node_color(self, node, color):
        node = self.normalize_node(node)
        if not node in self.colors:
            self.colors[node] = []
        self.colors[node].append(color)

    def assign_edge_color(self, edge, color):
        if not edge in self.colors:
            self.colors[edge] = []
        self.colors[edge].append(color)

    def assign_word_color(self, index, color):
        index = str(index)
        if not index in self.colors:
            self.colors[index] = []
        self.colors[index].append(color)

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
        self.amr_struct = {}
        self.ud_lex = {}
        self.ud_struct = {}
        self.sent_lex = {}
        self.sent_struct = {}

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
                # print(line)
                # print(self.amr_lex, self.ud_lex)
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
                        if not node in self.amr_struct:
                            self.amr_struct[node] = []
                        self.amr_struct[node].append(index)
                    if AMR_Structure.EDGE_RE.match(x):
                        edge = None
                        if len(align_split)>i+1 and not AMR_Structure.EDGE_RE.match(align_split[i+1]):
                            edge = x+' '+align_split[i+1].split('/')[0].strip()
                        else:
                            edge = x
                        for node in node_list:
                            e = node.split('/')[0].strip()+' '+edge
                            if not e in self.amr_struct:
                                self.amr_struct[e] = []
                            self.amr_struct[e].append(index)
                # split ud align into edges and nodes
                ud_split = [x for x in re.findall('(' + self.UD_NODE_RE.pattern + '|' + self.UD_EDGE_RE.pattern + '|[^\s|()]+)',ud_align)]
                for i, x in enumerate(ud_split):
                    if self.UD_NODE_RE.match(x):
                        if not x in self.ud_struct:
                            self.ud_struct[x] = []
                        self.ud_struct[x].append(index)
                        x = x.split('/')[0]
                        if not x in self.sent_struct:
                            self.sent_struct[x] = []
                        self.sent_struct[x].append(index)
                # print(line)
                # print(self.amr_struct, self.ud_struct)

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
    amr_index = 1
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
                amr = AMR_Structure(AMR, sentence, amr_index)
                for node in align.amr_lex:
                    amr.assign_node_color(node, 'lex'+str(align.amr_lex[node]))
                for word in align.sent_lex:
                    amr.assign_word_color(int(word)-1, 'lex'+str(align.sent_lex[word]))
                # structural alignments
                for x in align.amr_struct:
                    for i in align.amr_struct[x]:
                        if not ' ' in x:
                            amr.assign_node_color(x, 's'+str(i))
                        else:
                            amr.assign_edge_color(x, 's'+str(i))
                for word in align.sent_struct:
                    for i in align.sent_struct[word]:
                        amr.assign_word_color(int(word) - 1, 's'+str(i))
                html_output += amr.html()
                amr_index += 1
            AMR = ''


with open(html_file, 'w', encoding='utf8') as f:
    f.write(html_start+html_output+html_end)