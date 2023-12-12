from Jlib import *
lines = read_file("aoc9.txt")
lines = [list(map(int,i.split())) for i in lines]
c = 0
c2 = 0
for l in lines:
    d = [l]
    while True:
        k = []
        for i,v in enumerate(d[-1][:-1]):
            k.append(d[-1][i+1]-d[-1][i] )
        d.append(k)
        if all(kk==0 for kk in k):break
    d = d[::-1]
    prev = 0
    prev2 =0
    for i,v in enumerate(d):
        try:
            prev = v[-1]+prev
            prev2 = v[0]-prev2
        except: pass;
    c+=prev
    c2 += prev2
print("PART ONE:",c)
print("PART TWO:",c2)
