#!/usr/bin/env python3

import sys
import math

COUNT_LIST = []

for line in sys.stdin:
    line = line.strip()
    COUNT_LIST.append(int(line))

COUNT_SUM = sum(COUNT_LIST)
TOTAL_COUNTS = len(COUNT_LIST)
MEAN = math.floor(COUNT_SUM / TOTAL_COUNTS)
VAR = math.floor(sum([(count-MEAN)**2 for count in COUNT_LIST]) / TOTAL_COUNTS)
print(f'Mean\t{MEAN}')
print(f'Sum\t{sum(COUNT_LIST)}')
print(f'Min\t{min(COUNT_LIST)}')
print(f'Max\t{max(COUNT_LIST)}')
print(f'Var\t{VAR}')
