import CLASSE as C
import RACE as R
import MOB
import M_TYPE as M
import OTH
import perso as P
import Int_main


OK1 = False
to_print = "Classe ? : "
for i in C.liststr:
    to_print += i + ", "
print(to_print)
while not OK1:
    sub = OTH.nomag
    for i in C.listfunc:
        R1 = str(input())
        if R1 == i.CLASSE:
            classe = i
            OK1 = True
            break
    if not OK1:
        print("huh?")
print("OK")
if classe.CLASSE == "MAGE":
    to_print = "Type ? : "
    for s in M.liststr:
        to_print += s + ", "
    print(to_print)
    while not OK1:
        for f in M.listfunc:
            R2 = str(input())
            if R2 == str(f.TYPE):
                OK1 = True
                sub = f
                break
        if not OK1:
            print("huh?")
to_print = "Race ? : "
for s in R.liststr:
    to_print += s + ", "
print(to_print)
OK2 = False
while not OK2:
    for i in R.listfunc:
        R3 = str(input())
        if R3 == i.RACE:
            race = i
            OK2 = True
            break
    if not OK2:
        print("huh?")
print("OK")
ally_list = {}
mob_list = {}
new_list = {}
PJ = P.monperso(classe, race, sub)
PJ.present()
mob = MOB.MOB()
Turn = 0
your_turn = True
mob.new()
auto_turn = OTH.autoturn()
while True:
    if PJ.PV <= 0:
        OTH.you_lose()
    if mob.PV <= 0:
        mob.die()
    print("?")
    if your_turn:
        Int_main.interpret(input())
    else:
        mob.attack()
        auto_turn(False)
        your_turn = True
