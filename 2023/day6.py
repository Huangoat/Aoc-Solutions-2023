from Jlib import *
lines = read_file("aoc6.txt")

def calc_ways(time, record):
    w = 0
    for i in range(time):
        rt = time - i 
        distance = i * rt
        if distance > record:
            w += 1
    return w

times = list(map(int,lines[0].split()[1:]))
records = list(map(int,lines[1].split()[1:]))
tw = 1
for i in range(len(times)):
    w = calc_ways(times[i], records[i])
    tw *= w
t2,r2=int("".join(lines[0].split()[1:])),int("".join(lines[1].split()[1:]))

print("PART ONE:",tw)
print("PART TWO:", calc_ways(t2,r2))
