import regex as re
from collections import defaultdict
import functools

file = '7/test.txt'
file = '7/in.txt'

val = 0

rankings ='AKQT98765432J'

handRankings = ['five', 'four', 'fullhouse', 'three', 'two', 'one', 'high']

def getHandType(hand):
    counts = defaultdict(int)
    for h in hand: 
        counts[h] = counts[h]+1
    if len(counts) == 1 :
        return "five"
    if len(counts) == 2:
        if 'J' in counts.keys():
            return 'five'
        for c in counts:
            if counts[c] == 4:
                return "four"
        return "fullhouse"
    if len(counts) == 3 :
        twocount = 0
        for c in counts:
            if counts[c] == 3:
                if 'J' in counts.keys():
                    return "four"
                else:
                    return "three"
            if counts[c] == 2:
                twocount +=1
        if twocount == 2:
            if 'J' in counts.keys():
                if counts['J'] == 2:
                    return 'four'
                else:
                    return "fullhouse"
            else:
                return "two"
    if len(counts) == 4:
        if 'J' in counts.keys():
            return "three"
        return "one"
    if 'J' in counts.keys():
        return "one"
    return "high"

def rankHand(handt1, handt2): 
    hand1 = handt1[0]
    hand2 = handt2[0]
    type1 = getHandType(hand1)
    type2 = getHandType(hand2)

    if handRankings.index(type1) < handRankings.index(type2):
        return 1
    if handRankings.index(type2) < handRankings.index(type1):
        return -1
    
    for i in range(len(hand1)):
        if hand1[i] == hand2[i]:
            continue
        if rankings.index(hand1[i]) < rankings.index(hand2[i]):
            return 1
        else: 
            return -1 
    
    
hands = []


with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        hands.append(line.split(' '))

sortedhands = sorted(hands, key=functools.cmp_to_key(rankHand))

for i in range(len(sortedhands)):
    val += (int(sortedhands[i][1]) * (i+1))

print(val)
