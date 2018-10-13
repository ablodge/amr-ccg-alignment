import os, re
from utils.ccg import *
from utils.amr import *
from main import *

amr_file = r'data/aligned_amrs.txt'
sent_file = r'data/ccg.txt'
template_file = r'template.html'
html_file = r'demo_v2.html'

def main():
    generate_html(CCG_Lexical, amr_file, sent_file, template_file, html_file)
if __name__ == "__main__":
    main()


