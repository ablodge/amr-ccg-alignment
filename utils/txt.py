import html, re, sys
sys.path.append("../")


class TXT:

    ELEM_RE = re.compile(r'(\s+|\S+)')
    elem = None

    def __init__(self, text):
        self.text = text
        self.elem = self.init_elements()


    def init_elements(self):
        return [html.escape(t) for t in self.ELEM_RE.findall(self.text)]

    def elements(self):
        return self.elem

    def elements_html(self):
        elem = self.elements()
        j = 0
        for i, e in enumerate(elem):
            if e.strip():
                elem[i] = f'<word class="aligned {j}"><tok>{j}/</tok>{e}</word> '
                j += 1
        return elem

    def html(self):
        return '\n<pre>\n'+''.join(t for t in self.elements_html()).strip()+'\n</pre>\n'


    def __str__(self):
        return self.text

    @staticmethod
    def test(text):
        return True

    @classmethod
    def finditer(cls, text):
        for text in re.split('\n\s*\n', text):
            text = text.strip()
            if text and cls.test(text):
                yield text


def main():
    test_file = r'../data/amr_sentences.txt'

    with open(test_file, 'r', encoding='utf8') as f:
        for html in TXT.finditer(f.read()):
            html = TXT(html)
            print(html.html())

if __name__=="__main__":
    main()