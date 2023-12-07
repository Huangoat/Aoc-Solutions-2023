from Jlib import *
from copy import deepcopy

def make_str(prev_map, num):
    for i in prev_map:
        if num>=i[1]and num<=i[1]+i[2]-1:
            return i[0]+(num-i[1])
    return num



def p1():
    lines = open("aoc5.txt","r").read().split("\n\n")
    k = ([i.split("\n")for i in lines])
    prev_map = []
    s = k[0][0].split("seeds: ")[1].split()
    k[-1].pop(-1)
    seeds = [int(i) for i in s]


    for i,v in enumerate(k):
        if i==0:continue
        ns = []
        for s in seeds:
            ns.append(make_str(prev_map, s))
        seeds = deepcopy(ns)
        new_map = []
        for ii,vv in enumerate(v):
            if ii==0: continue
            a, b, c = [int(l) for l in vv.split()]
            new_map.append([a, b, c])

        prev_map = deepcopy(new_map)

    ns = []
    for s in seeds:
        ns.append(make_str(prev_map, s))
    seeds = deepcopy(ns)
    print("PART ONE:", min(seeds))



def p2():
    lines = open("aoc5.txt","r").read().split("\n\n")
    k = ([i.split("\n")for i in lines])
    prev_map = []
    s = k[0][0].split("seeds: ")[1].split()
    k[-1].pop(-1)
    s = [int(i) for i in s]
    seeds = []
    for i,v in enumerate(s):
        print("SEED", i+1,end=" | ")
        if i%2==1: continue
        for z in range(s[i], s[i]+s[i+1]+1):
            seeds.append(z)

    print("Seed List finished")
    for i,v in enumerate(k):
        print("COUNTER:", i+1)
        if i==0:continue
        ns = []
        for s in seeds:
            ns.append(make_str(prev_map, s))
        seeds = deepcopy(ns)
        new_map = []
        for ii,vv in enumerate(v):
            if ii==0: continue
            a, b, c = [int(l) for l in vv.split()]
            new_map.append([a, b, c])

        prev_map = deepcopy(new_map)

    ns = []
    for s in seeds:
        ns.append(make_str(prev_map, s))
    seeds = deepcopy(ns)
    print("PART TWO:", min(seeds))
p1()
p2()
