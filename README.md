# Major General

A Major System memory tool. Type a number, tap between digits to cut it into pieces,
and pick a word for each piece. The words are sorted most-common first.

Open `index.html` from any static server (it fetches `words.txt`):

    python3 -m http.server   # then visit http://localhost:8000

## Data

`words.txt` has one line per digit code: `code word word ...`.
`tools/build_words.py` builds it from the
[CMU Pronouncing Dictionary](https://github.com/cmusphinx/cmudict) (sounds, not spelling)
and the [FrequencyWords](https://github.com/hermitdave/FrequencyWords) English subtitle counts:

    python3 tools/build_words.py cmudict.dict en_full.txt > words.txt

Key: 0 s z · 1 t d th · 2 n ng · 3 m · 4 r · 5 l · 6 j sh ch zh · 7 k g · 8 f v · 9 p b
