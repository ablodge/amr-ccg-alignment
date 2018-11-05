import re, os
from amr import *

os.chdir(r'..\data')

ud_align_file = 'amr_ud_alignments.txt'
empty_align_file = 'empty_alignments.txt'
output_file = 'amr_ccg_alignments.txt'

ud_aligns = {}
ud_aligns_structural = {}
amrs = {}
ccgs = {}
sents = {}
ccg_aligns = {}

# get AMRs, CCGs
with open(empty_align_file, 'r', encoding='utf8') as f:
    examples = f.read().replace('\r', '').split('\n\n')
    for i, ex in enumerate(examples):
        ex = ex.replace('# AMR:', '') \
            .replace('# CCG:', '') \
            .replace('# Alignments:', '') \
            .replace('# ', '')
        if not ex.strip():
            continue
        split = ex.split('\n\n')
        amr, ccg_tags, ccg_words = split[1], split[2].split('\t'), split[3].split('\t')
        sent = ' '.join(w.split('/')[1] for w in ccg_words if w).strip()
        amrs[sent] = amr
        ccgs[sent] = [t for t in ccg_tags if t]
        sent_num = split[0]
        sents[sent_num] = sent

# get ud alignments
with open(ud_align_file, 'r', encoding='utf8') as f:
    exs = f.read().replace('\r', '')
    exs = re.split(r'\n\s*\n', exs)
    i = 1
    for ex in exs:
        Sent_RE = re.compile('# ::snt (?P<sent>.*?)\n')
        sent = Sent_RE.search(ex).group('sent')
        lines = ex.split('\n')
        ud_aligns[sent.replace(' ','')] = []
        ud_aligns_structural[sent.replace(' ','')] = []

        for line in lines:
            if re.match('[0-9]+[.]', line): continue
            if line.strip().startswith('#'): continue
            if not line: continue
            if not '#' in line: continue
            amr, ud = line.split('#')[0], line.split('#')[1]
            amr = amr.strip()
            ud = ud.strip()
            if ' ' in amr and ':name'==amr.split()[1]:
                amr = amr.replace('(','').replace(')','').replace('|','')
                amr = [a for a in amr.split()]
                amr = ' '.join(amr)
                ud = ud.replace('(','').replace(')','').replace('|','')
                ud = ' '.join(u for u in ud.split() if not u.startswith(':'))
                ud_aligns_structural[sent.replace(' ','')].append(ud + ' ~ ' + amr)
                continue
            if ' ' in amr or ' ' in ud: continue
            if amr.startswith('none'): continue
            amr = amr.split('/')[0]
            # ud = ud.split('/')[1]
            ud_aligns[sent.replace(' ','')].append(ud + ' ~ ' + amr)
        i += 1


def get_modifier(amr, amr_node, ccg_tag):
    Mod_RE = re.compile(f'^[a-z][0-9]*_:?mod_{amr_node}$')
    syn_args = int(ccg_tag.split(':')[1]) if ':' in ccg_tag else 0

    is_modifier = any(Mod_RE.match(e) and syn_args == 1 for i, e in amr.edges())
    if is_modifier:
        amr_align = [amr_node] + [e for i, e in amr.edges() if Mod_RE.match(e)]
        return ' '.join(amr_align) + '     # Modifier (converted from ud)'
    return


def get_verb(amr, amr_node, ccg_tag):
    ARG_RE = re.compile(f'^({amr_node}_:?ARG[0-9]_[a-z][0-9]*|[a-z][0-9]*_:?ARG[0-9]-of_{amr_node})$')
    syn_args = int(ccg_tag.split(':')[1]) if ':' in ccg_tag else 0
    sem_args = [e for i, e in amr.edges() if ARG_RE.match(e)]
    has_args = len(sem_args) == syn_args and sem_args
    if has_args:
        amr_align = [amr_node] + sem_args
        return ' '.join(amr_align) + '     # Predicate (converted from ud)'
    return

def get_noun(ccg_tag):
    syn_args = int(ccg_tag.split(':')[1]) if ':' in ccg_tag else 0
    if syn_args == 0:
        amr_align = [amr_node]
        return ' '.join(amr_align) + '     # (converted from ud)'
    return


def get_name(amr, amr_nodes, ud_nodes):
    # get nodes
    # get edges

    ...
    return ' '.join(amr_align) + '     # Named Entity (converted from ud)'


num_sentences = len(ud_aligns)
for sent_num in sents:
    sent = sents[sent_num]
    # print(sent_num,sent)
    if not sent.replace(' ','') in ud_aligns:
        print('Skipping:',sent_num,sent)
        continue
    if not len(sent.split()) == len(ccgs[sent]):
        print('Skipping:',sent_num,sent)
        continue
    amr = AMR(amrs[sent], 0)
    ccg_aligns[sent_num] = [sent_num+'\n']
    for ud_align in ud_aligns[sent.replace(' ','')]:
        ud = ud_align.split(' ~ ')[0]
        ud_word = ud.split('/')[1]
        ud_id = int(ud.split('/')[0])

        amr_node = ud_align.split(' ~ ')[1]

        word_id = max(ud_id-1, 0)
        word_id = min(word_id, len(sent.split())-1)

        ccg_word = sent.split()[word_id]
        ccg_tag = ccgs[sent][word_id]
        # handle mismatched indices
        if not ccg_word.lower().startswith(ud_word):
            word_ids = [j for j, w in enumerate(sent.lower().split()) if w.startswith(ud_word.lower())]
            if not word_ids: continue
            word_id = word_ids[0]
            ccg_word = sent.split()[word_id]
            ccg_tag = ccgs[sent][word_id]

        word = sent.split()[word_id]

        # get patterns
        verb = get_verb(amr, amr_node, ccg_tag)
        mod = get_modifier(amr, amr_node, ccg_tag)
        noun = get_noun(ccg_tag)

        if verb:
            amr_align = verb
        elif mod:
            amr_align = mod
        elif noun:
            amr_align = noun
        else:
            continue
        # print(ccg_word,'~',amr_align)
        ccg_aligns[sent_num].append(str(word_id)+' ~ '+amr_align+'\n')

with open(output_file, 'w', encoding='utf8') as f:
    for num in ccg_aligns:
        f.write(''.join(ccg_aligns[num]) + '\n')
