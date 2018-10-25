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
        elems = self.elements()
        for i,e in enumerate(elems):
            if re.match('<L.*?>', e):
                e = e.split()[1]
                w, t = e.split(':')[0], e.split(':')[1]
                w = f'<td><word class="aligned" tok-id="{j}"><tok>{j}/</tok>{w}</word> </td>'
                tag = t
                t = self.clean_tag(t)
                t = f'<td class="constit" colspan="1"><tag class="aligned" tok-id="{j}">{t}</tag> </td>'
                words.append(w)
                tags.append(t)
                elems[i] = str(j) + '=' +tag
                j += 1
            elif e=='(':
                elems[i] = '<*>'
            elif e ==')':
                elems[i] = '</*>'

        elems = ''.join(elems)

        Parens_RE = re.compile('<\*>(?P<text>[^*]*)</\*>')
        i = 1
        while '<*>' in elems:
            for p in Parens_RE.finditer(elems):
                text = p.group('text')
                elems = elems.replace(p.group(), f'<{i}>{text}</{i}>', 1)
            i += 1
        max = i
        j = 1
        while j <= max:
            constits.append([])
            Word_RE = re.compile(f'<{j}>(?P<a>[0-9]+)=(?P<tag>\S*?)</{j}>')
            Unary_RE = re.compile(f'<{j}>U:(?P<tag>\S+) (?P<a>[0-9]+(:[0-9]+)?)=(?P<tag1>\S+?) ?</{j}>')
            Binary_RE = re.compile(f'<{j}>H(?P<lg>[<>]):(?P<tag>\S*?) (?P<a>[0-9]+(:[0-9]+)?)=(?P<tag1>\S*?) (?P<b>[0-9]+(:[0-9]+)?)=(?P<tag2>\S*?) ?</{j}>')

            while re.search(f'<{j}>', elems):
                regex = re.search(f'<{j}>.*?</{j}>', elems).group()
                if Word_RE.match(regex):
                    a = Word_RE.match(regex).group('a')
                    tag = Word_RE.match(regex).group('tag')
                    elems = Word_RE.sub(a+'='+tag, elems, 1)
                elif Unary_RE.match(regex):
                    tag_dirty = Unary_RE.match(regex).group('tag')
                    tag = self.clean_tag(tag_dirty)
                    a = Unary_RE.match(regex).group('a')
                    elems = Unary_RE.sub(a+'='+tag_dirty, elems, 1)
                    if ':' in a:
                        start, end = int(a.split(':')[0]), int(a.split(':')[1])
                        size = end - start
                    else:
                        start, end = int(a), int(a)+1
                        size = 1
                    prev_tag = Unary_RE.match(regex).group('tag1')
                    combin = self.combinator_unary(prev_tag, tag_dirty)
                    c = f'<td class="constit ccg-parse" colspan="{size}" span="{start}:{end}">{tag}<span class="combinator">{combin}</span></td>'
                    constits[j-1].append(c)
                elif Binary_RE.match(regex):
                    x = Binary_RE.match(regex)
                    tag_dirty = x.group('tag')
                    tag = self.clean_tag(tag_dirty)
                    a = x.group('a')
                    b = x.group('b')
                    if ':' in a:
                        a = a.split(':')[0]
                    if ':' in b:
                        b = b.split(':')[1]
                    else:
                        b = str(int(b)+1)
                    elems = Binary_RE.sub(a+':'+b+'='+tag_dirty, elems, 1)
                    size = int(b) - int(a)
                    tag1 = Binary_RE.match(regex).group('tag1')
                    tag2 = Binary_RE.match(regex).group('tag2')
                    combin = self.combinator_binary(tag1,tag2,tag_dirty)
                    c = f'<td class="constit ccg-parse" colspan="{size}" span="{a}:{b}">{tag}<span class="combinator">{combin}</span></td>'
                    constits[j - 1].append(c)

                else:
                    print(j, regex)
            j += 1
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

    def combinator_binary(self, tag1, tag2, tag):

        FA_RE1 = re.compile(r'(?P<X>\S+)[*]/[*](?P<Y>\S+)')
        FA_RE2 = re.compile(r'(?P<X>\S+)[*]\\[*](?P<Y>\S+)')
        B_RE = re.compile(r'(?P<X>\S+)[*][\\/][*](?P<Y>\S+)')
        # assign combinator
        tag1 = re.sub(r'\[.*?\]', '', tag1)
        tag2 = re.sub(r'\[.*?\]', '', tag2)
        tag = re.sub(r'\[.*?\]', '', tag)
        combin = ''
        m = FA_RE1.match(self.mark_first_arg(tag1))
        m2 = FA_RE2.match(self.mark_first_arg(tag2))
        # Function Application
        if m:
            Y = m.group('Y')
            X = m.group('X')
            if Y in [tag2, f'({tag2})'] and X in [tag, f'({tag})']:
                combin = '&gt;'
        if m2:
            Y = m2.group('Y')
            X = m2.group('X')
            if Y in [tag1, f'({tag1})'] and X in [tag, f'({tag})']:
                combin = '&lt;'
        # Other
        if tag1 in ['.', ',', '?', 'LRB', 'RRB']:
            combin = tag1
        if tag2 in ['.', ',', '?', 'LRB', 'RRB'] or not tag2.strip():
            combin = tag2
        if not tag1.strip() or not tag2.strip():
            combin = 'SPACE'
        if tag1 == 'conj' and tag in [tag2 + '\\' + tag2, f'({tag2})\\({tag2})']:
            combin = 'conj'
        # Composition
        if (not combin) and B_RE.match(self.mark_first_arg(tag1)) \
                and B_RE.match(self.mark_first_arg(tag2)) \
                and B_RE.match(self.mark_first_arg(tag)):
            a = B_RE.match(self.mark_first_arg(tag1))
            b = B_RE.match(self.mark_first_arg(tag2))
            c = B_RE.match(self.mark_first_arg(tag))
            X1 = a.group('X')
            Y1 = a.group('Y')
            X2 = b.group('X')
            Y2 = b.group('Y')
            X3 = c.group('X')
            Y3 = c.group('Y')
            if Y1 == X2 and X1 == X3 and Y2 == Y3:
                combin = 'B&lt;'
            elif X1 == Y2 and X3 == X2 and Y1 == Y3:
                combin = 'B&lt;'
            else:
                print('B?', tag1, '+', tag2, '=>', tag)
                print('X1 ', X1, 'Y1 ', Y1)
                print('X2 ', X2, 'Y2 ', Y2)
                print('X3 ', X3, 'Y3 ', Y3)
        if not combin:
            print('B?', tag1, '+', tag2, '=>', tag)
            combin = '?'
        return combin


    def combinator_unary(self, tag1, tag2):
        TR_RE1 = re.compile(r'(?P<T1>\S+)/[(](?P<T2>\S+)\\(?P<X>\S+)[)]')
        TR_RE2 = re.compile(r'(?P<T1>\S+)\\[(](?P<T2>\S+)/(?P<X>\S+)[)]')

        # assign combinator
        combin = '?'
        tag1 = re.sub(r'\[.*?\]', '', tag1)
        tag2 = re.sub(r'\[.*?\]', '', tag2)
        if TR_RE1.match(tag2) and TR_RE1.match(tag2).group('T1') == TR_RE1.match(tag2).group('T2'):
            X = TR_RE1.match(tag2).group('X')
            if X == tag1 or X == '(' + tag1 + ')':
                combin = 'TR&gt;'
            else:
                print('U?', tag1, '=>', tag2)
        elif TR_RE2.match(tag2) and TR_RE2.match(tag2).group('T1') == TR_RE2.match(tag2).group('T2'):
            X = TR_RE2.match(tag2).group('X')
            if X == tag1 or X == '(' + tag1 + ')':
                combin = 'TR&lt;'
            else:
                print('U?', tag1, '=>', tag2)
        elif tag1 == 'N' and tag2 == 'NP':
            combin = 'NP'
        elif re.match(r'S(\[.*?\])?[\\/]NP', tag1):
            if re.match(r'NP?[\\/]NP?', tag2):
                combin = 'Rel'
            elif re.match(r'S[\\/]S', tag2):
                combin = 'AdvCl'
            else:
                print('U?', tag1, '=>', tag2)
        else:
            print('U?', tag1, '=>', tag2)
        return combin

    def clean_tag(self, tag):
        tag = super(CCG,self).clean_tag(tag)
        return tag.replace('[','<sub>').replace(']','</sub>')

    def mark_first_arg(self,tag):
        depth = 0
        for i,c in enumerate(tag):
            if c == '(':
                depth +=1
            elif c == ')':
                depth -=1
            elif c in ['\\','/'] and depth==0:
                return tag[:i]+'*'+tag[i]+'*'+tag[i+1:]
        return tag

def main():
    test_file = r'../data/ccg.txt'

    with open(test_file, 'r', encoding='utf8') as f:
        for ccg in CCG.finditer(f.read()):
            ccg = CCG(ccg)
            ccg.html()


if __name__ == "__main__":
    main()