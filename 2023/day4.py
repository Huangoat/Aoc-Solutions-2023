from Jlib import *
lines = read_file("aoc4.txt")
copies = {}
p1 = 0
for ind,i in enumerate(lines):
    try:copies[ind] += 1
    except:copies[ind]=1
    m2 = i.split(" | ")[1].split()
    m1 = i.split(" | ")[0].split()
    m1 = [c for c in m1 if c.isnumeric()]
    m3 = int(i.split(": ")[0].split("Card ")[1])
    k = len([ii for ii in m2 if ii in m1])
    kk=len([kk for kk in m2 if kk in m1])
    if kk!=0:p1+=2**(kk-1)
    for a in range(k):
        try:copies[a+1+ind] += copies[ind]
        except:copies[a+1+ind] = copies[ind];
print("PART ONE:",p1)
print("PART TWO:",sum(copies.values()))
