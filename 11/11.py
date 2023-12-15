import regex as re
from collections import defaultdict
from itertools import combinations
import functools
import math
from enum import Enum


file = '11/test.txt'
file = '11/in.txt'

val = 0
grid = []

galaxies = []

def distance(a,b):
    return sum(abs(x-y) for x, y in zip(a,b))
               
cols = set()

with open(file, 'r') as f:
    lines = f.readlines()
    colExpansion = set()
    rowExpansion = set()
    num = 0 
    for line in lines:
        line = line.strip()
        grid.append(line.strip())
        if '#' not in line:
            rowExpansion.add(num)
        else:
            col = 0
            for x in line:
                if x == '#':
                    cols.add(col)
                    galaxies.append((col,num))
                col +=1
        num +=1

colExpansion = set(list(range(len(grid[0]))))
colExpansion = colExpansion-cols
expansion = 1000000

combos = combinations(galaxies,2)
for combo in combos:
    cur = distance(combo[0],combo[1])
    for col in colExpansion:
        if min(combo[0][0], combo[1][0]) <=col <=max(combo[0][0], combo[1][0]):
            cur += expansion
    for row in rowExpansion:
        if min(combo[0][1], combo[1][1]) <=row <=max(combo[0][1], combo[1][1]):
            cur += expansion
    val += cur
print(val)