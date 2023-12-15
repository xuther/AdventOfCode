import regex as re
from collections import defaultdict
import functools
import math

file = '9/test.txt'
file = '9/in.txt'

val = 0

def getDiffs(line):
    diffs = []
    for i in range(len(line)-1):
        diffs.append(line[i+1] - line[i])
    return diffs

def iterate(line):
    readings = [line]
    while not all(i == readings[-1][0] for i in readings[-1]):
        readings.append(getDiffs(readings[-1]))

    next = 0
    for i in range(len(readings)):
        next = readings[-(i+1)][0] - next
    return next

with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        f = [int(i) for i in line.split(' ')]
        c = iterate(f)
        val += c
print(val)



