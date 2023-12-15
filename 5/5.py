import regex as re

file = '5/test.txt'
file = '5/in.txt'

seeds = []
seed_to_soil= {}
soil_to_fert= {}
fert_to_wat= {}
wat_to_light={}
light_to_temp= {}
temp_to_humidity= {}
humidity_to_location= {}

highLoc=0

def traverse_back(src, num):
    for k in src:
        if num >= src[k] and num <= src[k] + k[1]:
            return num + (k[0] - src[k]) 
    return num


def traverse(src, num):
    n = int(num)
    for k in src: 
        if n >= k[0] and n <= k[0] + k[1]:
            return src[k] + n - k[0]
    return n

def find(seedNum):
    a = traverse(seed_to_soil, seedNum)
    b = traverse(soil_to_fert, a)
    c = traverse(fert_to_wat, b)
    d = traverse(wat_to_light, c)
    e = traverse(light_to_temp, d)
    f = traverse(temp_to_humidity, e)
    g = traverse(humidity_to_location, f)
    return g

def find_inverted(val):
    a = traverse_back(humidity_to_location,val)
    b = traverse_back(temp_to_humidity,a)
    c = traverse_back(light_to_temp, b)
    d = traverse_back(wat_to_light, c)
    e = traverse_back(fert_to_wat, d)
    f = traverse_back(soil_to_fert, e)
    g = traverse_back(seed_to_soil, f)
    return g

val = 0
with open(file, 'r') as f:
    lines = f.read()
    splits = lines.split('\n\n')
    
    seeds = re.findall('(\d+ \d+)', splits[0]) 

    sts = splits[1].split('\n')[1:]
    for line in sts:
        vals = re.findall('(\d+)', line)
        seed_to_soil[(int(vals[1]), int(vals[2]))] = int(vals[0])
    sts = splits[2].split('\n')[1:]
    for line in sts:
        vals = re.findall('(\d+)', line)
        soil_to_fert[(int(vals[1]), int(vals[2]))] = int(vals[0])
    sts = splits[3].split('\n')[1:]
    for line in sts:
        vals = re.findall('(\d+)', line)
        fert_to_wat[(int(vals[1]), int(vals[2]))] = int(vals[0])
    sts = splits[4].split('\n')[1:]
    for line in sts:
        vals = re.findall('(\d+)', line)
        wat_to_light[(int(vals[1]), int(vals[2]))] = int(vals[0])
    sts = splits[5].split('\n')[1:]
    for line in sts:
        vals = re.findall('(\d+)', line)
        light_to_temp[(int(vals[1]), int(vals[2]))] = int(vals[0])
    sts = splits[6].split('\n')[1:]
    for line in sts:
        vals = re.findall('(\d+)', line)
        temp_to_humidity[(int(vals[1]), int(vals[2]))] = int(vals[0])
    sts = splits[7].split('\n')[1:]
    for line in sts:
        vals = re.findall('(\d+)', line)
        humidity_to_location[(int(vals[1]), int(vals[2]))] = int(vals[0])
        if int(vals[0]) + int(vals[2]) > highLoc:
            highLoc = int(vals[0]) + int(vals[2]) 

curBest = 1000000000000000000

for seed in seeds: 
    seedParts = seed.split(' ')
    for i in seedParts:
        cur = i
        q = find(cur)
        if q < curBest:
            curBest = q

print(curBest)

from queue import Queue
from multiprocessing import pool
import threading

outqueue = Queue()
statqueue = Queue()

p = pool.ThreadPool()
statusLock = threading.Lock()
status = [0 for i in range(p._processes)]

def checkSeeds(val):
    for i in seeds:
        p = [int(j) for j in i.split(' ')]
        if val >= p[0] and val < p[0] + p[1]:
            return True
    return False

def findReverse(cur):   
    val = find_inverted(cur)
    if checkSeeds(val):
        outqueue.put((cur,val))

def lookAtRange(vals):
    start,offset = vals[0], vals[1]
    for i in range(start, highLoc, offset):
        findReverse(i)
        if i %1000 == 0:
            outqueue.put((-1, i))
            statusLock.acquire()
            status[offset] = i
            statusLock.release()
    outqueue.put((-1, "done " + str(start)))

p.imap(lookAtRange, [(i, 15) for i in range(15)])

curBest = 100000000000000
curBestSeed = 0
counter = 0
while True:
    c = outqueue.get()
    if c[0] == -1:
        print("at: ", c[1])
    else:
        if c[0] < curBest:
            curBest = c[0]
            curBestSeed = c[1]
        print("found!", c)
        counter+=1
        if counter % 100 == 0:
            found = True
            statusLock.acquire()
            for i in status:
                if i < curBest:
                    found = False
            statusLock.release()
            if not found:
                break

outqueue.join() 
while not outqueue.empty():
    c = outqueue.get()
    if c[0] < curBest:
        curBest = c[0]
        curBestSeed = c[1]

print("best: ,", curBest, " seed: ", curBestSeed)
