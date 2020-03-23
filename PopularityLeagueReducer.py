#!/usr/bin/env python3

import sys

league_dict = {}

for line in sys.stdin:
    league_id, count = line.strip().split('\t')
    count = int(count)
    league_dict[league_id] = count

sorted_league_dict = sorted(league_dict.items(), key=lambda x: x[0], reverse=True)

for league_id, count in sorted_league_dict:
    print(f'{league_id}\t{count}')
