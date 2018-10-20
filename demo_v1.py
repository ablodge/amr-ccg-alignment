import os, re
from utils.txt import *
from utils.amr import *
from main import *


amr_file = r'data/aligned_amrs.txt'
sent_file = r'data/amr_sentences.txt'
template_file = r'template.html'
html_file = r'demo_v1.html'


def main():
    generate_html(TXT, amr_file, sent_file, template_file, html_file, "Sentence")
if __name__ == "__main__":
    main()


