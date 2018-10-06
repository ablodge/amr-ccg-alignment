import re
from .text2html import Text2html


class CCG2html(Text2html):

    ELEM_RE = re.compile(r'(\t|\n|[^\n\t]+)')

    def __init__(self, text, id):
        super().__init__(text)
        self.text = text
        self.struct = self.ELEM_RE.findall(self.text)
        self.id = id

    def test(cls, text):
        ...

    def words(self):
        ...

    def html(self):
        ...


