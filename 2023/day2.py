import sys
from Jlib import *
lines = read_file("aoc2.txt")
t = 0
p2 = 0

for i, x in enumerate(lines):
    nl = x.strip().split(": ")[1].split("; ")
    for k in nl:
        r,g,b=0,0,0
        for ii in k.split(", "):
            if "red" in ii:r+=int(ii.split()[0])
            if "blue" in ii: b+=int(ii.split()[0])
            if "green" in ii: g+=int(ii.split()[0])
        if r>12 or b>14 or g>13:break
    else:t += i+1

for i, x in enumerate(lines):

    nl = x.strip().split(": ")[1].replace(";",",").split(",")
    nl = [i.strip() for i in nl]

    r,g,b=0,0,0
    for k in nl:
        for ii in k.split(", "):
            if "red" in ii:r=max(r,int(ii.split()[0]))
            if "blue" in ii: b=max(b,int(ii.split()[0]))
            if "green" in ii: g=max(g,int(ii.split()[0]))

    p2 += (r*g*b)
print("PART ONE:", t)
print("PART TWO:", p2)
