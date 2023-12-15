import regex as re

file = '3/test.txt'
file = 'in.txt'

dif = [-1,0,1]

val = 0

nonsymbolset = '0123456789.'


with open(file, 'r') as f:
    lines = f.readlines()

    linelen = len(lines[0])-1
    for i in range(len(lines)):
        num = ''
        adjacent = False
        for j in range(linelen):
            if lines[i][j] in '01234567890':
                num += lines[i][j]
                # Check to see if touches a *
                if i > 0:
                    #Check above
                    if j > 0:
                        if lines[i-1][j-1] not in nonsymbolset:
                            adjacent = True
                    if lines[i-1][j] not in nonsymbolset:
                        adjacent = True
                    if j < linelen:
                        if lines[i-1][j+1] not in nonsymbolset:
                            adjacent = True
                if j > 0:
                    if lines[i][j-1] not in nonsymbolset:
                            adjacent = True
                if lines[i][j] not in nonsymbolset:
                        adjacent = True
                if j < linelen:
                    if lines[i][j+1] not in nonsymbolset:
                        adjacent = True
                if i < len(lines)-1:
                    if j > 0:
                        if lines[i+1][j-1] not in nonsymbolset:
                            adjacent = True
                    if lines[i+1][j] not in nonsymbolset:
                        adjacent = True
                    if j < linelen:
                        if lines[i+1][j+1] not in nonsymbolset:
                            adjacent = True
            else:
                if num != '' and adjacent == True:
                    val += int(num)
                num = ""
                adjacent = False

print(val)
                    
            




