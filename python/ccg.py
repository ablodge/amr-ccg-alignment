import re, sys, html

sys.path.append("..")
from python.txt import *


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
                t = f'<td><tag class="aligned" tok-id="{j}">{t}</tag> </td>'
                j += 1
                words.append(w)
                tags.append(t)
        return ['<table>\n<tr>']+words+['</tr>\n<tr>']+tags+['</tr>\n</table>']

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
            tag = tag+':'+'<args>'+str(arg_count)+'</args>'
        elif tag=='conj':
            tag='conj:<args>2</args>'
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


class CCG(CCG_Lexical):
    # <table class="visccg wordsabove">
    # <tbody>
    # 	<tr><td>the</td> <td>dog</td> <td>bit</td> <td>John</td> </tr>
    # 	<tr>
    # 		<td class="constit" colspan="1">NP/N</td>
    # 		<td class="constit" colspan="1">N</td>
    # 		<td class="constit" colspan="1">(S\NP)/NP</td>
    # 		<td class="constit" colspan="1">NP<sub>+proper</sub></td>
    # 	</tr>
    # 	<tr>
    # 		<td class="constit" colspan="2">NP
    # 			<span class="combinator">&gt;</span>
    # 		</td>
    # 	</tr>
    # 	<tr>
    # 		<td class="constit" colspan="2">S/(S\NP)
    # 			<span class="sem"> : λp . λy. ∃x. dog′(x) ∧ p(x,y)</span>
    # 			<span class="combinator">T&gt;</span>
    # 		</td>
    # 	</tr>
    # 	<tr>
    # 		<td class="constit" colspan="3">S/NP
    # 			<span class="combinator">B&gt;</span>
    # 		</td>
    # 	</tr>
    # 	<tr>
    # 		<td class="constit" colspan="4">S
    # 			<span class="combinator">&gt;</span>
    # 		</td>
    # 	</tr>
    # </tbody>
    # </table>
    def elements_html(self):
        words = []
        tags = []
        constits = []
        j = 0
        depth = max = 0
        elems = self.elements()
        for i,e in enumerate(elems):
            if re.match('<L.*?>', e):
                elems[i]=str(j)
                e = e.split()[1]
                w, t = e.split(':')[0], e.split(':')[1]
                w = f'<td><word class="aligned" tok-id="{j}"><tok>{j}/</tok>{w}</word> </td>'
                t = self.clean_tag(t)
                t = f'<td class="constit" colspan="1"><tag class="aligned" tok-id="{j}">{t}</tag> </td>'
                j += 1
                words.append(w)
                tags.append(t)
            elif e =='(':
                depth+=1
                if depth>max: max = depth
                elems[i] = f'<{depth}>'
            elif e==')':
                elems[i] = f'</{depth}>'
                depth-=1
        elems = ''.join(elems)
        j = max
        while j > 0:
            constits.append([])
            Word_RE = re.compile(f'<{j}>(?P<a>[0-9]+)</{j}>')
            Unary_RE = re.compile(f'<{j}>U:(?P<tag>\S+) (?P<a>[0-9]+(:[0-9]+)?) ?</{j}>')
            Binary_RE = re.compile(f'<{j}>H(?P<lg>[<>]):(?P<tag>\S+) (?P<a>[0-9]+(:[0-9]+)?) (?P<b>[0-9]+(:[0-9]+)?) ?</{j}>')
            while re.search(f'<{j}>', elems):
                regex = re.search(f'<{j}>.*?</{j}>', elems).group()
                if Word_RE.match(regex):
                    a = Word_RE.match(regex).group('a')
                    elems = Word_RE.sub(a, elems, 1)
                elif Unary_RE.match(regex):
                    tag = Unary_RE.match(regex).group('tag')
                    tag = self.clean_tag(tag)
                    a = Unary_RE.match(regex).group('a')
                    elems = Unary_RE.sub(a, elems, 1)
                    if ':' in a:
                        start, end = int(a.split(':')[0]), int(a.split(':')[1])
                        size = end - start
                    else:
                        start, end = int(a), int(a)+1
                        size = 1
                    c = f'<td class="constit ccg-parse" colspan="{size}" span="{start}:{end}">{tag}<span class="combinator">TR</span></td>'
                    constits[max-j].append(c)
                elif Binary_RE.match(regex):
                    x = Binary_RE.match(regex)
                    tag = x.group('tag')
                    tag = self.clean_tag(tag)
                    a = x.group('a')
                    b = x.group('b')
                    lg = x.group('lg')
                    if ':' in a:
                        a = a.split(':')[0]
                    if ':' in b:
                        b = b.split(':')[1]
                    else:
                        b = str(int(b)+1)
                    lg = '&gt;' if lg=='>' else '&lt;'
                    elems = Binary_RE.sub(a+':'+b, elems, 1)
                    size = int(b) - int(a)
                    c = f'<td class="constit ccg-parse" colspan="{size}" span="{a}:{b}">{tag}<span class="combinator">{lg}</span></td>'
                    constits[max - j].append(c)
                else:
                    print(j, elems)
            j -= 1
        Span_RE = re.compile('span="(?P<a>[0-9]+):(?P<b>[0-9]+)"')
        for i,row in enumerate(constits):
            span_end = 0
            for j,con in enumerate(row):
                x = Span_RE.search(con)
                a = int(x.group('a'))
                b = int(x.group('b'))
                if a>span_end:
                    constits[i][j] = f'<td colspan="{a-span_end}" span="{span_end}:{a}"/>'+constits[i][j]
                span_end = b
        ccg_parse = ['<tr class="expand">'+''.join(c) +'</tr>\n' for c in constits]
        ccg_parse.reverse()
        html_elems = []
        html_elems += ['<button class="expand">CCG parse ▲</button><br/>']
        html_elems += ['<table class="visccg wordsbelow"><tbody>\n']
        html_elems += ccg_parse
        html_elems += ['<tr>\n'] + tags + ['</tr>\n']
        html_elems += ['<tr>\n'] + words + ['</tr>\n']
        html_elems += ['</tbody></table>']
        return html_elems

    def clean_tag(self, tag):
        tag = super(CCG,self).clean_tag(tag)
        return tag.replace('[','<sub>').replace(']','</sub>')

def main():
    test_file = r'../data/ccg.txt'

    with open(test_file, 'r', encoding='utf8') as f:
        for ccg in CCG_Lexical.finditer(f.read()):
            ccg = CCG_Lexical(ccg)
            print(ccg.html())


if __name__ == "__main__":
    main()