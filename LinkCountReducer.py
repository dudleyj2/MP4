#!/usr/bin/env python3

import sys

link_dict = {}

for line in sys.stdin:
    parent_id, child_link, count = line.strip().split('\t')
    link_dict[child_link] = link_dict.get(child_link, 0) + int(count)
    
for link, count in link_dict.items():
    print(f'{link}\t{count}')
