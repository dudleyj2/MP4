#!/usr/bin/env python3

import sys

word_dict = {}

for line in sys.stdin:
    line.strip()
    word, count = line.split('\t')
    word_dict[word] = word_dict.get(word, 0) + int(count)

sort_word_dict = sorted(word_dict, key=lambda x: word_dict.get(x), reverse=False)

for word in sort_word_dict[:10]:
    print("%s\t%d" % (word, word_dict.get(word)))
