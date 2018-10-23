import re, sys, html
sys.path.append("..")
from python.txt import *


class AMR(TXT):
    NODE_RE = re.compile('([a-z][0-9]*|none[0-9]+)( ?/ ?[A-Za-z-]+[0-9]*)')
    EDGE_RE = re.compile('(:[A-Za-z0-9-]+(-of)?)')
    ELEM_RE = re.compile(r'('+NODE_RE.pattern + '|' + EDGE_RE.pattern + '|' + '[()]' + '|'+'[^\s()]+'+'|'+'\s+'+')')

    def __init__(self, text, id):
        # remove comments
        text = '\n'.join([l for l in text.split('\n') if l.strip() and not l.strip().startswith('#')])
    
        super().__init__(text)
        # remove comments
        self.id = id
        # nodes
        self.node_list = [(i, x.split('/')[0].strip()) for i, x in enumerate(self.elements()) if self.NODE_RE.match(x)]
        for i, e in enumerate(self.elements()):
            if not re.match(r'^('+self.NODE_RE.pattern + '|' + self.EDGE_RE.pattern + '|[()]|\s+)$', e):
                if e in [n for x,n in self.nodes()]:
                    self.node_list.append((i, e))
                else:
                    j = 0
                    while 'x'+str(j) in [n for x,n in self.nodes()]: j+=1
                    self.node_list.append((i, 'x'+str(j)))
                    self.elements()[i] = 'x'+str(j)+' / '+self.elements()[i]
        # edges
        self.edge_list = []
        depth = -1
        parents = []
        last_node = None
        for i, x in enumerate(self.elements()):
            if x == '(':
                depth += 1
                parents.append(last_node)
            elif x == ')':
                depth -= 1
                parents.pop()
            if self.NODE_RE.match(x):
                last_node = x
                parents[depth] = x
            if self.EDGE_RE.match(x):
                src = self.normalize_node(parents[-1]) + '_'
                trg = ''
                for j in range(i + 1, len(self.elements())):
                    next = self.elements()[j]
                    if not next.strip(): continue
                    if next == '(': continue
                    if next == ')': break
                    if self.EDGE_RE.match(next): break
                    trg = '_' + self.normalize_node(next)
                self.edge_list.append((i, src + x + trg))

    def init_elements(self):
        return [html.escape(x[0]) for x in self.ELEM_RE.findall(self.text)]

    def nodes(self):
        return self.node_list

    def edges(self):
        return self.edge_list

    @staticmethod
    def normalize_node(node):
        return node.split('/')[0].strip()

    def elements_html(self):
        elem = self.elements()
        for i, n in self.nodes():
            elem[i] = f'<amr-node class="aligned" tok-id="{n}">{elem[i]}</amr-node>'
        for i, e in self.edges():
            e = e.replace(':','')
            elem[i] = f'<amr-edge class="aligned" tok-id="{e}">{elem[i]}</amr-edge>'
        return elem

    @staticmethod
    def test(text):
        # ignore comments
        text = '\n'.join([l for l in text.split('\n') if not l.strip().startswith('#')])
        if not text.strip().startswith('('): return False
        depth = 0
        for ch in text:
            if ch=='(': depth+=1
            if ch==')': depth-=1
            if depth<0: return False
        if not depth == 0: return False
        return True

def main():
    test_file = r'../data/aligned_amrs.txt'

    with open(test_file, 'r', encoding='utf8') as f:
        for amr in AMR.finditer(f.read()):
            amr = AMR(amr, 1)
            print(amr.html())


if __name__ == "__main__":
    main()