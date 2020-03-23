#!/usr/bin/env python3

import sys
import string

STOP_WORDS_PATH = sys.argv[1]
DELIMITERS_PATH = sys.argv[2]

with open(STOP_WORDS_PATH) as f:
    lines = f.readlines()
    STOP_WORDS = [line.strip() for line in lines]

with open(DELIMITERS_PATH) as f:
    DELIMITERS = f.readline()

for line in sys.stdin:
    line = line.strip()
    line = ''.join([char.lower() if char not in DELIMITERS else ' ' for char in line])
    words = [word for word in line.split() if word not in STOP_WORDS]
    words_no_stop = [word for word in words if word not in STOP_WORDS]
    for word in words_no_stop:
        print(f'{word}\t1')
