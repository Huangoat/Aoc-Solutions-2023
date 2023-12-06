from Jlib import *
from copy import deepcopy

lines=read_file("aoc1.txt")
a=["one","two","three","four","five","six","seven","eight","nine"]


nlines = []
for i in lines:
    k = deepcopy(i)
    k = k.replace("eightwo","82")
    k = k.replace("oneight","18")
    k=k.replace("twone","21")
    for x in a:
        k = k.replace(x,str(a.index(x)+1))
    nlines.append(k)


lines = ["".join([x for x in i if x.isnumeric()])for i in lines]
olines = ["".join([x for x in i if x.isnumeric()])for i in nlines]

c = 0
p1 = 0
for i,v in enumerate(lines):
    c += 10*int(v[0]) + int(v[-1])
    p1 += 10*int(olines[i][0])+int(olines[i][-1])
    
print("PART 1:", p1)
print("PART 2:", c)

