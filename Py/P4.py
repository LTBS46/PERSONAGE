import random as rng
from Py import prefab as p


class Carreau:
    def __init__(self, x, y):
        self.pos = p.vector2d(x, y)
        self.color = "V"


def printgrid():
    t.t1 = 1
    t.t2 = 1
    t.finish = False
    to_print = ""
    finpr = {}
    while not t.finish:
        for a in grid:
            if (a.pos.x == t.t1) and (a.pos.y == t.t2):
                to_print += a.color
                if a.pos.x == width:
                    finpr.__setitem__(to_print, finpr.__len__() + 1)
                    print(to_print)
                    to_print = ""
                    if a.pos.y == height:
                        t.finish = True
                    t.t1 = 1
                    t.t2 += 1
                else:
                    t.t1 += 1


def getcolor(x, y):
    OK2 = False
    for i in grid:
        if i.pos.x == x:
            if i.pos.y == y:
                OK2 = True
                return i.color
    if not OK2:
        return "V"


def is_empty(x, y):
    OK3 = False
    for i in grid:
        if i.pos.x == x:
            if i.pos.y == y:
                OK3 = True
                return i.color == "V"
    if not OK3:
        return False


t = p.temp
width = 6
height = 5
grid = {}
for l in p.iter_int(height):
    for c in p.iter_int(width):
        grid.__setitem__(Carreau(c + 1, l + 1), -1)
printgrid()
end = False
win = False
lose = False
your_turn = True
while not end:
    if win:
        print("you_win")
        end = True
    elif lose:
        print("you_lose")
        end = True
    elif not your_turn:
        OK4 = False
        while not OK4:
            pos = rng.randrange(1, 6)
            if is_empty(pos, 1):
                for i in grid:
                    if i.pos.x == pos and is_empty(i.pos.x, i.pos.y):
                        t.t2 = i
                t.t2.color = "R"
                your_turn = True
    elif str(input()) == "  ":
        if your_turn:
            print("to you to play")
            OK1 = False
            inp = None
            while not OK1:
                inp = input()
                if str(inp) == "exit":
                    exit()
                elif str(inp) == "print":
                    printgrid()
                elif str(inp) == "pass":
                    OK1 = True
                    your_turn = False
                elif (int(inp) <= 1) and (int(inp) >= 6):
                    for i in grid:
                        if i.pos.x == int(inp) and i.color == "V":
                            t.t1 = i
                    t.t1.color = "J"
                    your_turn = False
                    OK1 = True
    for i in grid:
        if i.color == "J":
            if getcolor(i.pos.x + 1, i.pos.y) == "J":
                if getcolor(i.pos.x + 2, i.pos.y) == "J":
                    if getcolor(i.pos.x + 3, i.pos.y) == "J":
                        win = True
            elif getcolor(i.pos.x + 1, i.pos.y + 1) == "J":
                if getcolor(i.pos.x + 2, i.pos.y + 2) == "J":
                    if getcolor(i.pos.x + 3, i.pos.y + 3) == "J":
                        win = True
            elif getcolor(i.pos.x + 1, i.pos.y - 1) == "J":
                if getcolor(i.pos.x + 2, i.pos.y - 2) == "J":
                    if getcolor(i.pos.x + 3, i.pos.y - 3) == "J":
                        win = True
            elif getcolor(i.pos.x, i.pos.y + 1) == "J":
                if getcolor(i.pos.x, i.pos.y + 2) == "J":
                    if getcolor(i.pos.x, i.pos.y + 3) == "J":
                        win = True
        elif i.color == "R":
            if getcolor(i.pos.x + 1, i.pos.y) == "R":
                if getcolor(i.pos.x + 2, i.pos.y) == "R":
                    if getcolor(i.pos.x + 3, i.pos.y) == "R":
                        lose = True
            elif getcolor(i.pos.x + 1, i.pos.y + 1) == "R":
                if getcolor(i.pos.x + 2, i.pos.y + 2) == "R":
                    if getcolor(i.pos.x + 3, i.pos.y + 3) == "R":
                        lose = True
            elif getcolor(i.pos.x + 1, i.pos.y - 1) == "R":
                if getcolor(i.pos.x + 2, i.pos.y - 2) == "R":
                    if getcolor(i.pos.x + 3, i.pos.y - 3) == "R":
                        lose = True
            elif getcolor(i.pos.x, i.pos.y + 1) == "R":
                if getcolor(i.pos.x, i.pos.y + 2) == "R":
                    if getcolor(i.pos.x, i.pos.y + 3) == "R":
                        lose = True