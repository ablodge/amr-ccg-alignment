import re, sys, html

sys.path.append("..")
from python.txt import *

TAG_SET = set()


class CCG(TXT):
    ELEM_RE = re.compile(r'<.*?>|[()]|[^\s()]+|\s+')

    def __init__(self, text):
        # remove comments
        text = '\n'.join([l for l in text.split('\n') if l.strip() and not l.strip().startswith('#')])

        super().__init__(text)

    def init_elements(self):
        elem = []
        for e in self.ELEM_RE.findall(self.text):
            elem.append(e)
        return elem

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

    def elements_html(self):
        WORDS = []
        TAGS = []
        PHRASES = []
        CCG = self.elements()

        for i, e in enumerate(CCG):
            if e == '(':
                CCG[i] = '<*>'
            elif e == ')':
                CCG[i] = '</*>'

        CCG = ''.join(CCG)

        # find words
        j = 0
        for word in CCGBankUtils.word_iter(CCG):
            w = word.group('word')
            tag = word.group('tag')
            tag = CCGTagUtils.clean_parens(tag)
            pos = word.group('pos')
            CCG = CCG.replace(word.group(), f'{j}={tag}', 1)
            tag = CCGTagUtils.to_html(tag)
            WORDS.append(f'<td><word class="aligned" tok-id="{j}"><tok>{j}/</tok>{w}</word> </td>')
            TAGS.append(f'<td class="constit" colspan="1"><tag class="aligned" tok-id="{j}">{tag}</tag> </td>')
            j += 1

        # mark depth from inside out
        Parens_RE = re.compile('<\*>(?P<text>[^*]*)</\*>')
        i = 1
        while '<*>' in CCG:
            for p in Parens_RE.finditer(CCG):
                text = p.group('text')
                CCG = CCG.replace(p.group(), f'<{i}>{text}</{i}>', 1)
            i += 1
        max = i

        # Find Constituents from inside out
        j = 1
        while j <= max:
            PHRASES.append([])
            id_marker = lambda x, y: f'(?P<{x}>[0-9]+(:[0-9]+)?)=(?P<{y}>\S*?)'
            tag_pattern = CCGBankUtils.phrase_re().pattern
            Word_RE = re.compile(f'<{j}>{id_marker("a","tag")}</{j}>')
            Unary_RE = re.compile(f'<{j}>{tag_pattern} {id_marker("a","tag1")} ?</{j}>')
            Binary_RE = re.compile(f'<{j}>{tag_pattern} {id_marker("a","tag1")} {id_marker("b","tag2")} ?</{j}>')

            while re.search(f'<{j}>', CCG):
                regex = re.search(f'<{j}>.*?</{j}>', CCG).group()
                if Word_RE.match(regex):
                    a = Word_RE.match(regex).group('a')
                    tag = Word_RE.match(regex).group('tag')
                    CCG = Word_RE.sub(a + '=' + tag, CCG, 1)
                elif Unary_RE.match(regex):
                    tag = Unary_RE.match(regex).group('tag')
                    tag = CCGTagUtils.clean_parens(tag)
                    a = Unary_RE.match(regex).group('a')
                    CCG = Unary_RE.sub(a + '=' + tag, CCG, 1)
                    if ':' in a:
                        start, end = int(a.split(':')[0]), int(a.split(':')[1])
                        size = end - start
                    else:
                        start, end = int(a), int(a) + 1
                        size = 1
                    prev_tag = Unary_RE.match(regex).group('tag1')
                    combin = CCGTagUtils.get_combinator_unary(prev_tag, tag)
                    tag = CCGTagUtils.to_html(tag)
                    c = f'<td class="constit ccg-parse" colspan="{size}" span="{start}:{end}">{tag}<span class="combinator">{combin}</span></td>'
                    PHRASES[j - 1].append(c)
                elif Binary_RE.match(regex):
                    x = Binary_RE.match(regex)
                    tag = x.group('tag')
                    tag = CCGTagUtils.clean_parens(tag)
                    a = x.group('a')
                    b = x.group('b')
                    if ':' in a:
                        a = a.split(':')[0]
                    if ':' in b:
                        b = b.split(':')[1]
                    else:
                        b = str(int(b) + 1)
                    CCG = Binary_RE.sub(a + ':' + b + '=' + tag, CCG, 1)
                    size = int(b) - int(a)
                    tag1 = Binary_RE.match(regex).group('tag1')
                    tag2 = Binary_RE.match(regex).group('tag2')
                    combin = CCGTagUtils.get_combinator_binary(tag1, tag2, tag)
                    tag = CCGTagUtils.to_html(tag)
                    c = f'<td class="constit ccg-parse" colspan="{size}" span="{a}:{b}">{tag}<span class="combinator">{combin}</span></td>'
                    PHRASES[j - 1].append(c)

                else:
                    raise Exception('Parsing CCG error:', j, regex)
            j += 1
        Span_RE = re.compile('span="(?P<a>[0-9]+):(?P<b>[0-9]+)"')
        for i, row in enumerate(PHRASES):
            span_end = 0
            for j, con in enumerate(row):
                x = Span_RE.search(con)
                a = int(x.group('a'))
                b = int(x.group('b'))
                if a > span_end:
                    PHRASES[i][j] = f'<td colspan="{a-span_end}" span="{span_end}:{a}"/>' + PHRASES[i][j]
                span_end = b
        ccg_parse = ['<tr class="expand">' + ''.join(c) + '</tr>\n' for c in PHRASES]
        ccg_parse.reverse()
        html_elems = []
        html_elems += ['<button class="expand">CCG parse ▲</button><br/>']
        html_elems += ['<div class="scroll">']
        html_elems += ['<table class="visccg wordsbelow"><tbody>\n']
        html_elems += ccg_parse
        html_elems += ['<tr>\n'] + TAGS + ['</tr>\n']
        html_elems += ['<tr>\n'] + WORDS + ['</tr>\n']
        html_elems += ['</tbody></table>']
        html_elems += ['</div>']
        return html_elems

    # Example of ccg in html:
    #
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


class CCGTagUtils:

    @staticmethod
    def clean_parens(tag):
        tag = CCGTagUtils.mark_depth(tag)
        max = CCGTagUtils.get_max_depth(tag)
        j = 1
        while j <= max:
            Left_RE = re.compile(f'^(?P<pre>(<[0-9]+>|[(])*)<{j}>(?P<a>.*?)</{j}>')
            Right_RE = re.compile(f'<{j}>(?P<a>.*?)</{j}>')
            Modifier_RE = re.compile(fr'<{j}>(?P<a>.*?)</{j}>(?P<slash>[/\\])<{j}>(?P<b>.*?)</{j}>')
            while re.search(f'<{j}>', tag):
                mod = Modifier_RE.search(tag)
                if mod and CCGTagUtils.remove_features(mod.group('a')) == CCGTagUtils.remove_features(mod.group('b')):
                    a = mod.group('a')
                    b = mod.group('b')
                    slash = mod.group('slash')
                    tag = tag.replace(mod.group(), '(' + a + ')' + slash + '(' + b + ')')
                elif Left_RE.match(tag):
                    x = Left_RE.match(tag)
                    pre = x.group('pre')
                    a = x.group('a')
                    tag = tag.replace(x.group(), pre + a)
                elif Right_RE.search(tag):
                    x = Right_RE.search(tag)
                    a = x.group('a')
                    tag = tag.replace(x.group(), '(' + a + ')')
            j += 1
        tag = tag.replace(r'((S\NP)/NP)', r'(S\NP/NP)')
        # print(tag)
        return tag

    @staticmethod
    def to_html(tag):
        x = CCGTagUtils.mark_depth(tag)
        i = 1
        while f'<{i}>' in tag:
            Paren_RE = re.compile(f'<{i}>.*?</{i}>')
            while Paren_RE.search(x):
                x = Paren_RE.sub('X', x)
            i += 1
        arg_count = len(re.findall(r'[/\\]', x))

        if arg_count > 0:
            tag = tag + ':' + '<args>' + str(arg_count) + '</args>'
        elif tag == 'conj':
            tag = 'conj:<args>2</args>'
        return tag.replace('[', '<sub>').replace(']', '</sub>')

    @staticmethod
    def mark_depth(tag):
        Paren_RE = re.compile('^(?P<pre>([^()])*)(?P<paren>[()])')
        i = 0
        while Paren_RE.match(tag):
            s = Paren_RE.match(tag).group('pre')
            p = Paren_RE.match(tag).group('paren')
            if p == '(':
                i += 1
                tag = Paren_RE.sub(s + f'<{i}>', tag, 1)
            else:
                tag = Paren_RE.sub(s + f'</{i}>', tag, 1)
                i -= 1
        return tag

    @staticmethod
    def get_max_depth(deep_tag):
        i = 1
        max = 0
        while f'<{i}>' in deep_tag:
            max = i
            i += 1
        if '<1>' not in deep_tag:
            return -1
        return max

    @staticmethod
    def unmark_depth(deep_tag):
        i = 1
        tag = deep_tag
        while f'<{i}>' in tag:
            tag = tag.replace(f'<{i}>', '(')
            tag = tag.replace(f'</{i}>', ')')
            i += 1
        return tag

    @staticmethod
    def mark_first_arg(tag):
        depth = 0
        index = -1
        for i, c in enumerate(tag):
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            elif c in ['\\', '/'] and depth == 0:
                index = i
        if index > 0:
            return tag[:index] + '*' + tag[index] + '*' + tag[index + 1:]
        return tag

    @staticmethod
    def add_indices(tag):
        ...

    @staticmethod
    def remove_features(tag):
        return re.sub(r'\[.+?\]', '', tag)

    @staticmethod
    def get_combinator_unary(before_tag, after_tag):
        TR1_RE = re.compile(r'(?P<T1>\S+)/[(](?P<T2>\S+)\\(?P<X>\S+)[)]')
        TR2_RE = re.compile(r'(?P<T1>\S+)\\[(](?P<T2>\S+)/(?P<X>\S+)[)]')

        before_tag = CCGTagUtils.remove_features(before_tag)
        after_tag = CCGTagUtils.remove_features(after_tag)
        # Type Raising
        tr = TR1_RE.match(after_tag)
        if tr and tr.group('T1') == tr.group('T2'):
            X = tr.group('X')
            if X in [before_tag, f'({before_tag})']:
                return 'TR>'
        tr = TR2_RE.match(after_tag)
        if tr and tr.group('T1') == tr.group('T2'):
            X = tr.group('X')
            if X in [before_tag, f'({before_tag})']:
                return 'TR<'
        # Raising to NP
        if before_tag == 'N' and after_tag == 'NP':
            return 'NP'
        # Clauses
        if before_tag in ['S/NP', 'S\\NP']:
            if after_tag in ['N\\N', 'NP\\NP']:
                return 'Rel'
            if after_tag in ['S\\S', 'S/S']:
                return 'AdvCl'
            if after_tag == 'NP':
                return 'NomCl'
        print('U?', before_tag, '=>', after_tag)
        return '?'

    @staticmethod
    def get_combinator_binary(left_tag, right_tag, tag):
        FA1_RE = re.compile(r'(?P<X>\S+)[*]/[*](?P<Y>\S+)')
        FA2_RE = re.compile(r'(?P<X>\S+)[*]\\[*](?P<Y>\S+)')

        left_tag = CCGTagUtils.remove_features(left_tag)
        right_tag = CCGTagUtils.remove_features(right_tag)
        tag = CCGTagUtils.remove_features(tag)

        # Right Function Application
        fa = FA1_RE.match(CCGTagUtils.mark_first_arg(left_tag))
        if fa and CCGTagUtils.clean_parens(fa.group('Y')) == right_tag \
                and CCGTagUtils.clean_parens(fa.group('X')) in tag:
            return '>'
        # Left Function Application
        fa = FA2_RE.match(CCGTagUtils.mark_first_arg(right_tag))
        if fa and CCGTagUtils.clean_parens(fa.group('Y')) == left_tag \
                and CCGTagUtils.clean_parens(fa.group('X'))  == tag:
            return '<'

        # Other
        if left_tag in ['.', ',', '?', ';', ':', 'LRB', 'RRB', 'RQU']:
            return left_tag
        if right_tag in ['.', ',', '?', ';', ':', 'LRB', 'RRB', 'RQU']:
            return right_tag
        if left_tag == 'conj' and tag in [f'{right_tag}\\{right_tag}', f'({right_tag})\\({right_tag})']:
            return 'conj'
        # Composition
        B_RE = re.compile(r'(?P<X>\S+)[*][\\/][*](?P<Y>\S+)')

        l = B_RE.match(CCGTagUtils.mark_first_arg(left_tag))
        r = B_RE.match(CCGTagUtils.mark_first_arg(right_tag))
        t = B_RE.match(CCGTagUtils.mark_first_arg(tag))
        if l and r and t:
            lx, ly = CCGTagUtils.clean_parens(l.group('X')), CCGTagUtils.clean_parens(l.group('Y'))
            rx, ry = CCGTagUtils.clean_parens(r.group('X')), CCGTagUtils.clean_parens(r.group('Y'))
            tx, ty = CCGTagUtils.clean_parens(t.group('X')), CCGTagUtils.clean_parens(t.group('Y'))
            if ly == rx and lx == tx and ry == ty:
                return 'B>'
            elif lx == ry and rx == tx and ly == ty:
                return 'B<'
        if right_tag == r'S\S' and tag == left_tag:
            return 'B<$'
        if left_tag == r'S/S' and tag == right_tag:
            return 'B>$'
        print('B?', left_tag, '+', right_tag, '=>', tag)
        return '?'


class CCGBankUtils:

    @staticmethod
    def word_re():
        # <L N NN NN question N>
        return re.compile('<L [^\s>]+ [^\s>]+ [^\s>]+ [^\s>]+ [^\s>]+>')

    @staticmethod
    def phrase_re():
        # <T NP 0 2>
        return re.compile('<T (?P<tag>[^\s>]+) [^\s>]+ [^\s>]+>')

    @staticmethod
    def word_iter(ccg_code):
        return re.finditer('<L (?P<tag>[^\s>]+) (?P<pos>[^\s>]+) [^\s>]+ (?P<word>[^\s>]+) [^\s>]+>', ccg_code)

    @staticmethod
    def is_word(ccg_code):
        # <L N NN NN question N>
        return re.match('^<L [^\s>]+ [^\s>]+ [^\s>]+ [^\s>]+ [^\s>]+>$', ccg_code)

    @staticmethod
    def is_phrase(ccg_code):
        # <T NP 0 2>
        return re.match('^<T [^\s>]+ [^\s>]+ [^\s>]+>$', ccg_code)

    @staticmethod
    def get_tag(ccg_code):
        return ccg_code.split()[1]

    @staticmethod
    def get_word(ccg_code):
        return ccg_code.split()[4]

    @staticmethod
    def get_pos(ccg_code):
        return ccg_code.split()[2]


def main():
    test_file = r'../data/ccg.txt'

    with open(test_file, 'r', encoding='utf8') as f:
        for ccg in CCG.finditer(f.read()):
            ccg = CCG(ccg)
            ccg.html()
    # for tag in sorted(TAG_SET):
    #     print(tag)


if __name__ == "__main__":
    main()
