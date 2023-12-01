import regex as re

file = 'test.txt'
file = 'in.txt'

p1 = 0
p2 = 0
res = 0

digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

with open(file, 'r') as f:
    for line in f.readlines():
        matches = re.findall('(\d|one|two|three|four|five|six|seven|eight|nine)', line, overlapped=True)
        first = matches[0]
        if first in digits:
            first = digits[first]
        second = matches[len(matches)-1]
        if second in digits:
            second = digits[second]
        cur = int(first+second)
        res += cur
print(res)