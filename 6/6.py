import regex as re

file = '6/test.txt'
file = '6/in.txt'
val = 1

def calc_distance(racelen, holdDuration):
    return holdDuration * (racelen - holdDuration)

with open(file, 'r') as f:
    lines = f.readlines()

    times = re.findall('(\d+)', lines[0])
    distances = re.findall('(\d+)', lines[1])

    for i in range(len(times)):
        ways = 0
        for j in range(int(times[i])):
            distance = calc_distance(int(times[i]), j)
            if distance > int(distances[i]):
                ways += 1
        val *= ways

print(val)