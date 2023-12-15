import regex as re
from collections import defaultdict
from itertools import combinations
import functools
import math
from enum import Enum


file = '12/test.txt'
file = '12/in.txt'

val = 0


searched = {}
def find(line, counts, spot, curspring):
    state = (len(counts),spot,curspring)
    # have we already looked here?
    if state in searched:
        return searched[state]
    val = 0

    # base case
    if spot == len(line): 
        if len(counts) == 0 or (curspring == counts[0] and len(counts) == 1):
            counts = counts[1:]
            val += 1
        return val

    #need to split and decide if we place a . or a # here how we do it. 
    if line[spot] == "." or line[spot] == '?':
        if curspring == 0:
            val += find(line, counts, spot+1, curspring)
        else:
            # did we terminate the next spring?
            if curspring == counts[0]:
                val += find(line, counts[1:], spot+1, 0)
            # Oherwiswe we can kill this branch.
    if line[spot] == '#' or line[spot] == '?':
        if len(counts) > 0 and curspring != counts[0]:
            val += find(line, counts, spot+1, curspring+1)
        # lots of ways for this branch to die. 
    
    searched[state] = val
    return val

p1 = 0
p2 = 0
with open(file, 'r') as f:
    lines = f.readlines()

    for line in lines:
        searched.clear()
        line = line.strip()
        parts = line.split(' ')
        springs = [int(i) for i in parts[1].split(',')]
        p1 += find(parts[0], springs, 0, 0)
        p2 += find(parts[0] + '?' + parts[0] + '?' + parts[0] + '?' + parts[0] + '?' + parts[0], springs+springs+springs+springs+springs,0,0)

print(p1)
print(p2)