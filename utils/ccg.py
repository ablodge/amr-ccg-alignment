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
                w = f'<td><word class="aligned" tok-id="{j}"><tok>{j}/</tok>{w}</word> </td>'
                t = self.clean_tag(t)
                t = f'<td><tag class="aligned" tok-id="{j}">{t}</tag></td>'
                j += 1
                words.append(w)
                tags.append(t)
        return ['<table><tr>']+words+['</tr><tr>']+tags+['</tr></table>']

    def clean_tag(self, tag):
        Paren_RE = re.compile('^(?P<pre>([^()])*)(?P<paren>[()])')
        i = 0
        max = 0
        while Paren_RE.match(tag):
            s = Paren_RE.match(tag).group('pre')
            p = Paren_RE.match(tag).group('paren')
            if p=='(':
                i += 1
                if i>max:
                    max = i
                tag = Paren_RE.sub(s + f'<{i}>', tag, 1)
            else:
                tag = Paren_RE.sub(s + f'</{i}>', tag, 1)
                i -= 1
        j = max
        while j > 0:
            Left_RE = re.compile(f'^(?P<pre>(<[0-9]+>)*)<{j}>(?P<a>.*?)</{j}>')
            Right_RE = re.compile(f'<{j}>(?P<a>.*?)</{j}>')
            Modifier_RE = re.compile(fr'<{j}>(?P<a>.*?)</{j}>(?P<slash>[/\\])<{j}>(?P<b>.*?)</{j}>')
            while re.search(f'<{j}>',tag):
                mod = Modifier_RE.search(tag)
                if mod and mod.group('a')==mod.group('b'):
                    a = mod.group('a')
                    b = mod.group('b')
                    slash = mod.group('slash')
                    tag = Modifier_RE.sub('('+a+')'+slash+'('+b+')',tag,1)
                elif Left_RE.match(tag):
                    x = Left_RE.match(tag)
                    pre = x.group('pre')
                    a = x.group('a')
                    tag = Left_RE.sub(pre + a, tag, 1)
                elif Right_RE.search(tag):
                    x = Right_RE.search(tag)
                    a = x.group('a')
                    tag = Right_RE.sub('(' +a+ ')', tag, 1)
            j -= 1
        arg_count = 0
        x = tag
        Paren_RE = re.compile('[(].*?[)]')
        while Paren_RE.search(x):
            x = Paren_RE.sub('X', x)
        arg_count = len(re.findall(r'[/\\]', x))

        if arg_count>0:
            tag = tag+':'+str(arg_count)
        if tag=='conj':
            tag='conj:2'
        # print(tag)
        return tag

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