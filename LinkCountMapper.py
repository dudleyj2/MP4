#!/usr/bin/env python3

import sys

for line in sys.stdin:
    parent_id, child_links_str = line.strip().split(':')
    child_links = child_links_str.split()
    for c_link in child_links:
        print(f'{parent_id}\t{c_link}\t1')
