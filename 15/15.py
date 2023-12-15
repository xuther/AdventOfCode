
import regex as re
from collections import defaultdict
from itertools import combinations
import functools
import math
from enum import Enum


file = '15/test.txt'
file = '15/in.txt'

pattern = '([a-z]+)([-=])(\d+)?'


boxes = [[] for i in range(256)]

ans = 0

def hash(word):
    val = 0
    for char in word:
        val += ord(char)
        val = val * 17
        val = val % 256
    return val
    
with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        vals = line.split(',')
        
        for val in vals:
            matches = re.findall(pattern, val)
            box = hash(matches[0][0])
            label = matches[0][0]
            op = matches[0][1]
            focal = matches[0][2]

            if op == '-':
                for l in range(len(boxes[box])):
                    if label in boxes[box][l]:
                        boxes[box].remove(boxes[box][l])
                        break
            
            if op == "=":
                found = False
                for l in range(len(boxes[box])):
                    if label in boxes[box][l]:
                        found = True
                        boxes[box][l] = label + ':' + focal
                        break
                if not found:
                    boxes[box].append(label + ':' + focal)
    
    ans1 = 0
    for box in range(len(boxes)):
        for j in range(len(boxes[box])):
            ans1 += (1 + box) * (j+1) * int(boxes[box][j].split(':')[1])

print(ans1)




