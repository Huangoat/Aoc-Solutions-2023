from Jlib import *
lines = read_file("aoc3.txt")
lines = [list(i) for i in lines]
visited = set()

def find_word(x, y, board):
    yy = y
    while True:
        try:
            xx = board[x][yy-1]
            if xx.isnumeric():
                yy -= 1
            else: break
        except:break
    ax, ay = x, yy
    c = ""
    while True:
        try:
            xx = board[ax][ay]
            if xx.isnumeric() and (ax,ay) not in visited:c += xx;visited.add((ax,ay))
            else: break
            ay += 1
        except:break
    return c


total1 = 0
total = 0
    for y,ii in enumerate(i):
        if not lines[x][y].isnumeric() and lines[x][y]!="." and lines[x][y] not in visited:
            visited.add((x,y))
            answers = set()
            for a,b in [(0,1),(1,0),(-1,0),(0,-1),(-1,1),(1,-1),(1,1),(-1,-1)]:
                ax, ay = x+a, y+b
                if lines[ax][ay].isnumeric(): 
                    answers.add(find_word(ax, ay,lines))
            answers = [int(i) for i in answers if i.isnumeric()]
            total1 += sum(answers)
            if len(answers)==2:
                total += answers[0]*answers[1]
print("PART 1:",total1)
print("PART 2:",total)


