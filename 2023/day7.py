from Jlib import *
lines = read_file("aoc7.txt")
cards, bids = [],[]
from copy import deepcopy

ordering = [[5], [4, 1], [3, 2],[3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]
for i in lines : 
    a,b = i.split()
    cards.append(a)
    bids.append(int(b))
nc = []
nb = []
orgcards = deepcopy(cards)
kk = [2, 3, 4, 5, 6, 7, 8, 9, "T","J","Q","K","A"]
kk = list(map(str, kk))
def weight(x):
    l = []
    for i in x: 
        l.append(kk.index(str(i))+1)
    return l
def p1():
    l = [[],[],[],[],[], [],[]]
    for i in cards:
        order = sorted([i.count(b) for b in set(i)], reverse=True)
        o = ordering.index(order)
        l[o].append(i)
    final = []
    for i in l:
        k = sorted(i, key=lambda x:weight(x), reverse=True)
        for x in k:
            final.append(x)
    total = 0
    final  = final[::-1]
    for i,v in enumerate(final):
        total += (i+1)*bids[orgcards.index(v)]
    print(total)

def p2():
    l = [[],[],[],[],[], [],[]]
    for i in cards:
        orgi = deepcopy(i)
        if "J" in i:
            if i=="JJJJJ":i = "AAAAA"
            else:
                ki = i.replace("J","")
                maxn = 0
                maxo = ki[0]
                iss = sorted(list(set(ki)),reverse=True)
                for d in iss:
                    if ki.count(d)==maxn:
                        maxn = ki.count(d)
                        if kk.index(str(d))>kk.index(str(maxo)):maxo = str(d)
                    if i.count(d)>maxn:
                        maxn = ki.count(d)
                        maxo = str(d)
            i = i.replace("J", maxo)
        nc.append(i)
        nb.append(bids[orgcards.index(orgi)])
        order = sorted([i.count(b) for b in set(i)], reverse=True)
        o = ordering.index(order)
        l[o].append(i)
    final = []
    for i in l:
        
        k = sorted(i, key=lambda x:weight(x), reverse=True)
        for x in k:
            final.append(x)
    total = 0
    final  = final[::-1]
    for i,v in enumerate(final):
        total += (i+1)*nb[nc.index(v)]
    print(total)
p1()
p2()
