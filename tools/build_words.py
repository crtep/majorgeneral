"""Build words.txt for the Major System tool.

Inputs:
  cmudict.dict  - CMU Pronouncing Dictionary (github.com/cmusphinx/cmudict)
  freq.txt      - word frequency list, "word count" per line
                  (github.com/hermitdave/FrequencyWords, en_full.txt)

Output (stdout): one line per digit code, "code word word word ..."
words sorted most-common first.
"""
import re, sys
from collections import defaultdict

PHON = {
    'S': '0', 'Z': '0',
    'T': '1', 'D': '1', 'TH': '1', 'DH': '1',
    'N': '2', 'NG': '2',
    'M': '3',
    'R': '4', 'ER': '4',
    'L': '5',
    'JH': '6', 'CH': '6', 'SH': '6', 'ZH': '6',
    'K': '7', 'G': '7',
    'F': '8', 'V': '8',
    'P': '9', 'B': '9',
}
MIN_COUNT = 4

cmu_path, freq_path = sys.argv[1], sys.argv[2]
freq = {}
with open(freq_path, encoding='utf8') as f:
    for line in f:
        parts = line.split()
        if len(parts) == 2 and parts[1].isdigit():
            w, c = parts[0], int(parts[1])
            if c < MIN_COUNT:
                break
            freq.setdefault(w, c)

codes = defaultdict(dict)
with open(cmu_path, encoding='utf8') as f:
    for line in f:
        line = line.split('#')[0].strip()
        if not line:
            continue
        word, *phones = line.split()
        word = re.sub(r'\(\d+\)$', '', word)
        if not re.fullmatch(r"[a-z]+(?:'[a-z]+)?", word):
            continue
        c = freq.get(word)
        if not c:
            continue
        if len(word) == 1 and word not in ('a', 'i'):
            continue
        code = ''.join(PHON.get(re.sub(r'\d', '', p), '') for p in phones)
        # merge doubled identical consonant sounds across nothing (rare in CMU)
        codes[code][word] = c

for code in sorted(codes, key=lambda k: (len(k), k)):
    words = sorted(codes[code].items(), key=lambda kv: -kv[1])
    print((code or '-') + ' ' + ' '.join(w for w, _ in words))
