import re, sys, html
from text2html import Text2html


class UD2html(Text2html):
    HTML_END = '''<script language="JavaScript" type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/d3/4.10.0/d3.js"></script>\n'''+\
               '''<script language="JavaScript" type="text/javascript" src="arborator-draft.js"></script>\n'''
    HTML_START = '<script> new ArboratorDraft(); // Start </script>\n'


    ID = 0
    FORM = 1
    LEMMA = 2
    UPOS = 3
    XPOS = 4
    FEATS = 5
    HEAD = 6
    DEPREL = 7
    DEPS = 8
    MISC = 9

    ELEM_RE = re.compile(r'(\n|[^\n]+)')

    def __init__(self, text, id):
        super().__init__(text)
        self.id = id
        self.word_list = []#[x.split('\t')[self.FORM] for x in self.structure()]
        self.rel_list = []#[' '.join([x.split('\t')[self.ID], x.split('\t')[self.DEPREL], x.split('\t')[self.HEAD]]) for x in self.structure()]

    def init_structure(self, text):
        return [html.escape(x).replace('\r','') for x in self.ELEM_RE.findall(self.text)]

    @staticmethod
    def test(text):
        return bool(re.match(r'^((\S+\t){9}(\S+\t)*\S+\n)+$', text.strip()+'\n'))

    def words(self):
        return self.word_list

    def relations(self):
        return self.rel_list

    def html(self):
        return '\n<connl>' + super(UD2html,self).html() + '</connl>\n'


def main():
    test_file = 'test_ud.txt'
    color_word = 'fault'
    color_edge = ''

    text = open(test_file, 'r', encoding='utf8').read()
    print(UD2html.test(text))
    if UD2html.test(text):
        html = UD2html(text, 1)
        print(html.HTML_START + html.html() + html.HTML_END)


if __name__ == "__main__":
    main()
