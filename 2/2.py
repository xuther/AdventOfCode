import regex as re

file = '2/test.txt'
file = 'in.txt'

res = 0 

game = 0

cubes = {'red': 12, 'blue': 14, 'green': 13}
with open(file, 'r') as f:
    for line in f.readlines():
        minred = 0
        minblue = 0
        mingreen = 0
        game +=1
        possible = True
        newlines = line.split(';')
        for i in newlines:
            blue = re.findall('(\d+) blue', i)
            green = re.findall('(\d+) green',i)
            red = re.findall('(\d+) red',i)
            if len(blue) > 0 and int(blue[0]) > minblue:
                minblue = int(blue[0])
            if len(red) > 0 and int(red[0]) > minred:
                minred = int(red[0])
            if len(green) > 0 and int(green[0]) > mingreen:
                mingreen = int(green[0])
        res += mingreen * minred * minblue

print(res)