import regex as re
from collections import defaultdict
import functools
import math
from enum import Enum

file = '10/test.txt'
file = '10/in.txt'

UL = 'UL' 
UR = 'UR' 
DR = 'DR'
DL = 'DL'
UD = 'UD'
LR = 'LR'
GR = 'GR'
ST = 'S'

val = 0

pipes = {
    '|': UD,
    '-': LR,
    'L': UR,
    'J': UL,
    '7': DL,
    'F': DR,
    '.': GR,
    'S': ST,
}


grid = []
mainLoop = []
dirs = [(-1, 0), (0,1), (0,-1), (1,0)]

def At(pos):
    return grid[pos[0]][pos[1]]

def mainAt(pos):
    return mainLoop[pos[0]][pos[1]]

def getNext(pos, prev):
    valid = []
    cur = At(pos)
    ccur = grid[pos[0]][pos[1]]
    if 'R' in cur:
        valid.append((pos[0]+1, pos[1]))
    if 'L' in cur:
        valid.append((pos[0]-1, pos[1]))
    if 'U' in cur:
        valid.append((pos[0], pos[1]-1))
    if 'D' in cur:
        valid.append((pos[0], pos[1]+1))
    if prev in valid: valid.remove(prev)
    return valid[0]

def CalcVaildPipe(pos):
    valid = {UL, UR, DL, DR, LR, UD}
    # Get Surrounding pipes
    for v in dirs: 
        considerx = pos[0]+v[0] 
        considery = pos[1]+v[1]
        if considerx < 0 or considerx > len(grid)-1 or considery < 0 or considery > len(grid[0])-1:
            continue
        candidate = grid[considerx][considery]
        if considerx < pos[0]:
            if candidate not in [UR, DR, LR]:
                valid = valid - {LR,UL,DL}
            else:
                valid = valid - {UR, DR, UD}
        if considerx > pos[0]:
            if candidate not in [LR, UL, DL]:
                valid = valid - {UR, DR, UD}
            else:
                valid = valid - {UD,UL,DL}
        if considery < pos[1]:
            if candidate not in [UD, DL, DR]:
                valid = valid - {UD, UR, UL}
        if considery > pos[1]:
            if candidate not in [UD, UL, UR]:
                valid = valid - {UD, DR, DL}
        if considerx == 0:
            valid = valid - {LR, DL, UL}
        if considerx >= len(grid)-1:
            valid = valid - {LR, DR, UR}
        if considery == 0:
            valid = valid - {UD, UR, UL}
        if considery == len(grid[0])-1:
            valid = valid - {UD, DR, DL}
    return valid.pop()

start = (0,0)
with open(file, 'r') as f:
    lines = f.readlines()

    grid = [['.' for x in range(len(lines))] for y in range(len(lines[0].strip()))]
    mainLoop = grid
    for y in range(len(lines)):
        for x in range(len(lines[y].strip())):
            grid[x][y] = pipes[lines[y][x]]
            if grid[x][y] == ST:
                start = (x,y) 

grid[start[0]][start[1]] = CalcVaildPipe(start)

prev = start
cur = start 
cur = getNext(cur,prev)
count = 0

while cur != start:
    cur, prev = getNext(cur,prev), cur
    mainLoop[cur[0]][cur[1]] = At(cur)
    count+=1

print(count//2 + count %2)

for y in range(len(mainLoop[0])):
    count = 0
    for x in range(len(mainLoop)):
        if mainAt((x,y)) in [UD, UR, UL]:
            count +=1
        if mainAt((x,y)) == GR and count %2 == 1:
            val +=1


print(val)
print("start was :", CalcVaildPipe(start))
