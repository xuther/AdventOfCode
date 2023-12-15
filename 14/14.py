import regex as re
from collections import defaultdict
from itertools import combinations
import functools
import math
from enum import Enum


file = '14/test.txt'
#file = '14/in.txt'

val = 0

grid = []

ysize, xsize = 0,0

weight = 0

state = {}

def MoveRocksNorth():
    for y in range(ysize):
        for x in range(xsize):
            if grid[y][x] == 'O':
                global weight
                  #Scoot north
                tmp = y
                while tmp-1 >= 0 and grid[tmp-1][x] not in ['O', '#']:
                    tmp-=1
                
                grid[y][x] = '.'
                grid[tmp][x] = 'O'

def MoveRocksSouth():
    for y in range(ysize-1,-1,-1):
        for x in range(xsize):
            if grid[y][x] == 'O':
                global weight
                  #Scoot north
                tmp = y
                while tmp+1 < ysize and grid[tmp+1][x] not in ['O', '#']:
                    tmp+=1
                
                grid[y][x] = '.'
                grid[tmp][x] = 'O'

def MoveRocksWest():
    for y in range(ysize):
        for x in range(xsize):
            if grid[y][x] == 'O':
                global weight
                  #Scoot north
                tmp = x
                while tmp-1 >= 0 and grid[y][tmp-1] not in ['O', '#']:
                    tmp-=1
                
                grid[y][x] = '.'
                grid[y][tmp] = 'O'

def MoveRocksEast():
    for y in range(ysize):
        for x in range(xsize-1,-1,-1):
            if grid[y][x] == 'O':
                global weight
                  #Scoot north
                tmp = x
                while tmp+1 < xsize and grid[y][tmp+1] not in ['O', '#']:
                    tmp+=1
                
                grid[y][x] = '.'
                grid[y][tmp] = 'O'

def calcWeight():
    weight = 0
    for y in range(ysize):
        for x in range(xsize):
            if grid[y][x] == 'O':
                weight += ysize-y
    return weight

def checkForCycle(count):
    val = " ".join([' '.join(l) for l in grid])
    if val in state.keys():
        return state[val]
    state[val] = count
    return -1

with open(file, 'r') as f:
    lines = f.readlines()
    grid = [list(l.strip()) for l in lines ]
    ysize = len(grid)
    xsize = len(grid[0])
    MoveRocksNorth()
    print(calcWeight())

    grid = [list(l.strip()) for l in lines ]


    cycles = 1000000000
    for i in range(cycles):
        MoveRocksNorth()
        MoveRocksWest()
        MoveRocksSouth()
        MoveRocksEast()
        cycle = checkForCycle(i)
        if cycle == -1:
            continue
        # Project forward we can jump by whatever the interval is now until the end. 
        cycle_len = i - cycle

        left = ((cycles - i) % cycle_len) -1
        break

    for i in range(left):
        MoveRocksNorth()
        MoveRocksWest()
        MoveRocksSouth()
        MoveRocksEast()
    print(calcWeight())

