from Jlib import *
from collections import defaultdict
import math
import sys
from copy import deepcopy

sys.set_int_max_str_digits(100000000)
lines = read_file("aoc8.txt")[2:]
kins = list(read_file("aoc8.txt")[0])
d = {}
for i in lines:
    a, b = i.split(" = ")
    d[a] = b[1:-1].split(", ")


def p1():
    c = 0
    ins = deepcopy(kins)*100
    node = "AAA"
    while True:
        i = ins[0]
        if node=="ZZZ":break;c+=1
        if i=="L":node = d[node][0]
        if i=="R":node = d[node][1]
        c += 1
        ins.pop(0)
    print("PART ONE:", c)


def p2():
    ins = deepcopy(kins)
    nodes = [i for i in d if i[-1] == "A"]

    cc = 1
    ll = 0
    h = []
    for n in nodes:
        c = 0
        while True:
            try: i = ins[ll];ll += 1
            except: ll = 0;i = ins[ll];ll += 1
            if i == "L": n = d[n][0]
            elif i == "R":n = d[n][1]
            if n[-1] == "Z":c+=1;cc=math.lcm(cc, c); break
            c += 1
    print("PART 2:",cc)
p1()
p2()

