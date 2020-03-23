#!/usr/bin/env python3

import sys

league_path = sys.argv[1]
league_dict = {}

with open(league_path) as f:
    leagues = []
    for line in f:
        leagues.append(line.split()[0])
    for league in leagues:
        league_dict[league] = 0
    
for line in sys.stdin:
    parent_id, count = line.strip().split('\t')
    if parent_id in leagues:
        count = int(count)
        league_dict[parent_id] = count

for league, count in league_dict.items():
    print(f'{league}\t{count}')
