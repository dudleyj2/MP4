#!/usr/bin/env python3
  
import sys

link_dict = {}

for line in sys.stdin:
    parent_id, link_number = line.strip().split('\t')
    link_dict[parent_id] = link_dict.get(parent_id, 0) + int(link_number)

link_dict_items = link_dict.items()
sorted_link_dict = sorted(link_dict_items)

for link, count in sorted_link_dict:
    if link_dict.get(link) == 0:
        print(link)
