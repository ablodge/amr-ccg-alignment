import re, sys, html

sys.path.append("..")
from utils.txt import *


class CCG_Lexical(TXT):

    ELEM_RE = re.compile(r'<.*?>|[()]|[^\s()]+|\s+')

    def __init__(self, text):
        # remove comments
        text = '\n'.join([l for l in text.split('\n') if l.strip() and not l.strip().startswith('#')])

        super().__init__(text)

    def init_elements(self):
        elem = []
        for e in self.ELEM_RE.findall(self.text):
            if re.match(r'<L.*?>', e):
                s = e.split()
                e = '<L '+s[4]+':'+s[1]+' >'
            elif re.match(r'<T.*?>', e):
                tr = {'0 1>':'U',
                      '0 2>':'H<',
                      '1 2>':'H>'}
                s = e.split()
                e = tr[s[2]+' '+s[3]] + ':' + s[1]
            elem.append(e)
        return elem

    def elements_html(self):
        words = []
        tags = []
        j = 0
        for e in self.elements():
            if re.match('<L.*?>',e):
                e = e.split()[1]
                w, t = e.split(':')[0],e.split(':')[1]
                w = f'<td><word class="aligned {j}"><tok>{j}/</tok>{w}</word> </td>'
                t = f'<td><tag class="{j}">{t}</tag></td>'
                j += 1
                words.append(w)
                tags.append(t)
        return ['<table><tr>']+words+['</tr><tr>']+tags+['</tr></table>']

    @staticmethod
    def test(text):
        # ignore comments
        text = '\n'.join([l for l in text.split('\n') if not l.strip().startswith('#')])
        if not text.strip().startswith('('): return False
        depth = 0
        for ch in text:
            if ch == '(': depth += 1
            if ch == ')': depth -= 1
            if depth < 0: return False
        if not depth == 0: return False
        return True


def main():
    test_file = r'../data/ccg.txt'

    with open(test_file, 'r', encoding='utf8') as f:
        for ccg in CCG_Lexical.finditer(f.read()):
            ccg = CCG_Lexical(ccg)
            print(ccg.html())


if __name__ == "__main__":
    main()