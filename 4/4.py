import regex as re

file = '4/test.txt'
file = '4/in.txt'

val = 0
curCard = 0
with open(file, 'r') as f:
    lines = f.readlines()
    cardCounts = [1 for i in range(len(lines))]
    for line in lines:
        card = line.split(':')[1].split('|')
        wins = re.findall('(\d+)', card[0])
        nums = re.findall('(\d+)', card[1])

        cval = 0
        for n in nums:
            if n in wins:
                cval += 1  
        for i in range(cval):
            cardCounts[curCard+i+1] += 1 * cardCounts[curCard]
        curCard += 1


for i in cardCounts:
    val += i

print(val)



