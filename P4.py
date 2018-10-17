import prefab as p


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
    for i in grid:
        if i.pos.x == x:
            if i.pos.y == y:
                return i.color


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
        end = True
    elif lose:
        end = True
    elif input() != None:
        if your_turn:
            print("to you to play")
            OK1 = False
            inp = None
            while not OK1:
                inp = input()
                if (int(inp) <= 1) and (int(inp) >= 6) or str(inp) == "exit":
                    OK1 = True
            if str(inp) == "exit":
                exit()
            else:
                for i in grid:
                    if i.pos.x == int(inp) and i.color == "V":
                        i.color = "J"
                        your_turn = False
    for i in grid:
        if i.color == "J":
            if getcolor(i.pos.x + 1, i.pos.y) == "J":
                if getcolor(i.pos.x + 2, i.pos.y) == "J":
                    if getcolor(i.pos.x + 3, i.pos.y) == "J":
                        win = True
            elif getcolor(i.pos.x + 1, i.pos.y) == "J":
                if getcolor(i.pos.x + 2, i.pos.y) == "J":
                    if getcolor(i.pos.x + 3, i.pos.y) == "J":
        elif i.color == "R":

            if getcolor(i.pos.x + 1, i.pos.y) == "R":
                if getcolor(i.pos.x + 2, i.pos.y) == "R":
                    if getcolor(i.pos.x + 3, i.pos.y) == "R":
                        lose = True