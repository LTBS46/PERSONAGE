import CLASSE
import RACE as R
import MOB
import M_TYPE as M
import math
import ARME as A
import random as rng
import prefab as p


class monperso:
    def __init__(self, classe, race, sub):
        classe.__init__()
        race.__init__()
        self.CLASSE = classe
        self.RACE = race
        self.SUB = sub
        self.LVL = 1
        self.POS = p.vector2d(0, 0)
        self.calculEvery()

    def present(self):
        print("|--------------------------------------|")
        if self.SUB == "nul":
            self.to_print = "|Classe : " + self.CLASSE.CLASSE
            if not self.CLASSE.CLASSE == "Chevalier":
                if (self.CLASSE.CLASSE == "Rodeur") or (self.CLASSE.CLASSE == "Prêtre"):
                    self.to_print = self.to_print + "   "
                elif (self.CLASSE.CLASSE == "Paladin") or (self.CLASSE.CLASSE == "Sorcier"):
                    self.to_print = self.to_print + "  "
                else:
                    self.to_print = self.to_print + " "
            self.to_print = self.to_print + "      "
        else:
            if self.SUB.TYPE == "OMNI":
                self.to_print = "|Classe : " + self.CLASSE.CLASSE + " de " + self.SUB.TYPE
                self.to_print = self.to_print + "  "
            else:
                self.to_print = "|Classe : " + self.CLASSE.CLASSE + " de " + self.SUB.TYPE
                self.to_print = self.to_print + "   "
        if not self.RACE.RACE == "Mi-nain":
            if (self.RACE.RACE == "Ork") or (self.RACE.RACE == "Elf"):
                self.to_print = self.to_print + "    "
            elif self.RACE.RACE == "Nain":
                self.to_print = self.to_print + "   "
            else:
                self.to_print = self.to_print + " "
        self.to_print = self.to_print + "Race : " + self.RACE.RACE + "|"
        print(self.to_print)
        self.to_print = "|Niv : " + str(int(self.LVL))
        space = 7
        if not int(self.LVL) >= 100:
            space += 1
            if not int(self.LVL) >= 10:
                space += 1
        if not int(self.PV) >= 10:
            space += 1
        if not int(self.PVMAX) >= 10:
            space += 1
        if not int(self.MANAMAX) >= 10:
            space += 1
        if not int(self.MANA) >= 10:
            space += 1
        space_at_time = space / 2
        i = 0
        if float.is_integer(space_at_time):
            while not i == int(space_at_time):
                self.to_print = self.to_print + " "
                i += 1
        else:
            while not i == int(space_at_time + 1):
                self.to_print = self.to_print + " "
                i += 1
        self.to_print = self.to_print + "PV : " + str(int(self.PV)) + "/" + str(int(self.PVMAX))
        i = 0
        while not i == int(space_at_time):
            self.to_print = self.to_print + " "
            i += 1
        self.to_print += "MANA : " + str(int(self.MANA)) + "/" + str(int(self.MANAMAX)) + "|"
        print(self.to_print)
        self.to_print = "|XP : " + str(float.__round__(float(self.xp), 2)) + "/" + str(float.__round__(self.xp_need, 0))
        i = 5
        while not self.xp >= math.pow(10, i):
            if i == 0:
                i = -2
            else:
                self.to_print += " "
            i -= 1
        i = 5
        while not self.xp >= math.pow(10, i):
            if i == 0:
                i = 0
            else:
                self.to_print += " "
            i -= 1
        self.to_print += "|"
        print(self.to_print)
        print("|--------------------------------------|")
        print("|Attributs :                           |")
        self.to_print = "|FOR : "
        self.to_print += str(self.ATTFOR)
        if self.ATTFOR < 10:
            self.to_print += " "
        self.to_print += " MOD : "
        self.to_print += str(self.MODFOR)
        self.to_print += "      END : "
        self.to_print += str(self.ATTEND)
        if self.ATTEND < 10:
            self.to_print += " "
        self.to_print += " MOD : "
        self.to_print += str(self.MODEND)
        self.to_print += "|"
        print(self.to_print)
        self.to_print = "|DEX : "
        self.to_print += str(self.ATTDEX)
        if self.ATTDEX < 10:
            self.to_print += " "
        self.to_print += " MOD : "
        self.to_print += str(self.MODDEX)
        self.to_print += "      PER : "
        self.to_print += str(self.ATTPER)
        if self.ATTPER < 10:
            self.to_print += " "
        self.to_print += " MOD : "
        self.to_print += str(self.MODPER)
        self.to_print += "|"
        print(self.to_print)
        self.to_print = "|SAG : "
        self.to_print += str(self.ATTSAG)
        if self.ATTSAG < 10:
            self.to_print += " "
        self.to_print += " MOD : "
        self.to_print += str(self.MODSAG)
        self.to_print += "                      |"
        print(self.to_print)
        print("|--------------------------------------|")
        self.to_print = "|Epée à 1 main : "
        if self.EPEE1M:
            self.to_print += "OUI"
        else:
            self.to_print += "NON"
        self.to_print += "   Arballette : "
        if self.ARBALLETTE:
            self.to_print += "OUI"
        else:
            self.to_print += "NON"
        self.to_print += "|"
        print(self.to_print)
        self.to_print = "|Epée à 2 mains : "
        if self.EPEE2M:
            self.to_print += "OUI"
        else:
            self.to_print += "NON"
        self.to_print += "    Bouclier : "
        if self.BOUCLIER:
            self.to_print += "OUI"
        else:
            self.to_print += "NON"
        self.to_print += "|"
        print(self.to_print)
        self.to_print = "|Hache à 1 main : "
        if self.HACHE1M:
            self.to_print += "OUI"
        else:
            self.to_print += "NON"
        self.to_print += "       Dague : "
        if self.DAGUE:
            self.to_print += "OUI"
        else:
            self.to_print += "NON"
        self.to_print += "|"
        print(self.to_print)
        self.to_print = "|Hache à 2 mains : "
        if self.HACHE2M:
            self.to_print += "OUI"
        else:
            self.to_print += "NON"
        self.to_print += "      Baton : "
        if self.BATON:
            self.to_print += "OUI"
        else:
            self.to_print += "NON"
        self.to_print += "|"
        print(self.to_print)
        self.to_print = "|Marteau à 1 main : "
        if self.MARTEAU1M:
            self.to_print += "OUI"
        else:
            self.to_print += "NON"
        self.to_print += "       Arc : "
        if self.ARC:
            self.to_print += "OUI"
        else:
            self.to_print += "NON"
        self.to_print += "|"
        print(self.to_print)
        self.to_print = "|Marteau à 2 mains : "
        if self.MARTEAU2M:
            self.to_print += "OUI"
        else:
            self.to_print += "NON"
        self.to_print += "    Lance : "
        if self.LANCE:
            self.to_print += "OUI"
        else:
            self.to_print += "NON"
        self.to_print += "|"
        print(self.to_print)
        print("|--------------------------------------|")

    def take_damage(self, damage):
        damage -= self.MODEND
        if damage <= 0:
            pass
        elif damage >= self.TEND:
            damage -= self.TEND
            self.TEND = 0
            self.PV -= damage
            if self.PV <= 0:
                you_lose()
        else:
            self.TEND -= damage

    def regen_pv(self, regen):
        self.PV += regen
        if self.PV >= self.PVMAX:
            self.PV = regen

    def reset(self):
        self.TEND = self.ATTEND

    def gain_xp(self, xp):
        self.xp += xp
        if self.xp >= self.xp_need:
            self.lvl_up()

    def lvl_up(self):
        self.LVL += 1
        self.xp -= self.xp_need
        self.xp_need = math.pow(self.LVL, 2)
        print("Tu passe niveau : " + str(self.LVL) + "!")
        self.calculEvery()

    def attack(self):
        self.DEG = 0
        for e in self.e_a:
            self.LDEG = 4
            for i in e.DEG:
                self.DEG += rng.randrange(1, self.LDEG) * i
                self.LDEG += 2
        mob.take_damage(self.DEG)

    def calculEvery(self):
        self.calculBase()
        self.calculComp()
        self.calculMANA()
        self.calculARMOR()
        self.calculATT()
        self.calculWEAP()

    def calculBase(self):
        print("calcul des basique")
        self.xp_need = math.pow(self.LVL, 2)
        self.xp = 0
        self.PVMAX = self.CLASSE.PV * self.RACE.PV
        self.PV = self.PVMAX

    def calculComp(self):
        print("gestion des compétance")
        self.COMPBASE1 = self.CLASSE.COMPBASE1
        self.COMPBASE2 = self.CLASSE.COMPBASE2
        self.COMPBASE3 = self.CLASSE.COMPBASE3
        self.COMPBASE4 = self.CLASSE.COMPBASE4
        # self.COMPBASE5 = self.RACE.COMPBASE
        self.listcomp = {self.COMPBASE1, self.COMPBASE2, self.COMPBASE3, self.COMPBASE4}

    def calculMANA(self):
        print("gestion de la magie")
        if self.CLASSE.CLASSE == "MAGE":
            self.SUB.__init__()
            self.MANAMAX = self.CLASSE.MANA * self.RACE.MANA * self.SUB.MANA
        else:
            self.MANAMAX = self.CLASSE.MANA * self.RACE.MANA
        self.MANA = self.MANAMAX

    def calculARMOR(self):
        print("gestion des armures")
        self.OKDB = False
        for i in self.listcomp:
            if i.NAME == "Plus d'armure":
                self.OKDB = True
        if self.OKDB:
            if self.CLASSE.ARMOR == "L":
                self.LIGHT_ARMOR = self.RACE.AL * 4
                self.HEAVY_ARMOR = self.RACE.AH * 2
                self.CLOTH = self.RACE.AC * 2
            if self.CLASSE.ARMOR == "H":
                self.LIGHT_ARMOR = self.RACE.AL * 2
                self.HEAVY_ARMOR = self.RACE.AH * 4
                self.CLOTH = self.RACE.AC * 2
            if self.CLASSE.ARMOR == "C":
                self.LIGHT_ARMOR = self.RACE.AL * 2
                self.HEAVY_ARMOR = self.RACE.AH * 2
                self.CLOTH = self.RACE.AC * 4
        else:
            if self.CLASSE.ARMOR == "L":
                self.LIGHT_ARMOR = self.RACE.AL * 2
                self.HEAVY_ARMOR = self.RACE.AH
                self.CLOTH = self.RACE.AC
            if self.CLASSE.ARMOR == "H":
                self.LIGHT_ARMOR = self.RACE.AL
                self.HEAVY_ARMOR = self.RACE.AH * 2
                self.CLOTH = self.RACE.AC
            if self.CLASSE.ARMOR == "C":
                self.LIGHT_ARMOR = self.RACE.AL
                self.HEAVY_ARMOR = self.RACE.AH
                self.CLOTH = self.RACE.AC * 2

    def calculATT(self):
        print("gestion des attributs")
        print("calcul de la force")
        self.OKFOR = False
        for i in self.listcomp:
            if i.NAME == "Minimum de force":
                self.OKFOR = True
        self.ATTFOR = self.CLASSE.ATTFOR + self.RACE.ATTFOR
        if self.OKFOR and (self.ATTFOR < 14):
            self.ATTFOR = 14
        self.MODFOR = self.CLASSE.MODFOR + self.RACE.MODFOR
        if self.OKFOR and (self.MODFOR < 7):
            self.MODFOR = 7
        print("calcul de l'endurence")
        self.OKEND = False
        for i in self.listcomp:
            if i.NAME == "Minimum d'endurence":
                self.OKEND = True
        self.ATTEND = self.CLASSE.ATTEND + self.RACE.ATTEND
        if self.OKEND and (self.ATTEND < 14):
            self.ATTEND = 14
        self.MODEND = self.CLASSE.MODEND + self.RACE.MODEND
        if self.OKEND and (self.MODEND < 7):
            self.MODEND = 7
        self.TEND = self.ATTEND
        print("calcul de la dextérité")
        self.OKDEX = False
        for i in self.listcomp:
            if i.NAME == "Minimum de dextérité":
                self.OKDEX = True
        self.ATTDEX = self.CLASSE.ATTDEX + self.RACE.ATTDEX
        if self.OKDEX and (self.ATTDEX < 14):
            self.ATTDEX = 14
        self.MODDEX = self.CLASSE.MODDEX + self.RACE.MODDEX
        if self.OKDEX and (self.MODDEX < 7):
            self.MODDEX = 7
        print("calcul de la percéption")
        self.OKPER = False
        for i in self.listcomp:
            if i.NAME == "Minimum de perception":
                self.OKPER = True
        self.ATTPER = self.CLASSE.ATTPER + self.RACE.ATTPER
        if self.OKPER and (self.ATTPER < 14):
            self.ATTPER = 14
        self.MODPER = self.CLASSE.MODPER + self.RACE.MODPER
        if self.OKPER and (self.MODPER < 7):
            self.MODPER = 7
        print("calcul de la sagacité")
        self.OKSAG = False
        for i in self.listcomp:
            if i.NAME == "Minimum de sagacité":
                self.OKSAG = True
        self.ATTSAG = self.CLASSE.ATTSAG + self.RACE.ATTSAG
        if self.OKSAG and (self.ATTSAG < 14):
            self.ATTSAG = 14
        self.MODSAG = self.CLASSE.MODSAG + self.RACE.MODSAG
        if self.OKSAG and (self.MODSAG < 7):
            self.MODSAG = 7

    def calculWEAP(self):
        print("gestion de l'armement")
        self.EPEE1M = A.EPEE1M()
        self.EPEE1M.OK = self.CLASSE.EPEE1M and self.RACE.EPEE1M
        self.EPEE2M = A.EPEE2M()
        self.EPEE2M.OK = self.CLASSE.EPEE2M and self.RACE.EPEE2M
        self.HACHE1M = A.HACHE1M()
        self.HACHE1M.OK = self.CLASSE.HACHE1M and self.RACE.HACHE1M
        self.HACHE2M = A.HACHE2M()
        self.HACHE2M.OK = self.CLASSE.HACHE2M and self.RACE.HACHE2M
        self.MARTEAU1M = A.MARTEAU1M()
        self.MARTEAU1M.OK = self.CLASSE.MARTEAU1M and self.RACE.MARTEAU1M
        self.MARTEAU2M = A.MARTEAU2M()
        self.MARTEAU2M.OK = self.CLASSE.MARTEAU2M and self.RACE.MARTEAU2M
        self.LANCE = A.LANCE()
        self.LANCE.OK = self.CLASSE.LANCE and self.RACE.LANCE
        self.BOUCLIER = self.CLASSE.BOUCLIER and self.RACE.BOUCLIER
        self.DAGUE = A.DAGUE()
        self.DAGUE.OK = self.CLASSE.DAGUE and self.RACE.DAGUE
        self.ARC = A.ARC()
        self.ARC.OK = self.CLASSE.ARC and self.RACE.ARC
        self.BATON = A.BATON()
        self.BATON.OK = self.CLASSE.BATON and self.RACE.BATON
        self.ARBALLETTE = A.ARBALLETTE()
        self.ARBALLETTE.OK = self.CLASSE.ARBALLETTE and self.RACE.ARBALLETTE
        self.tt_arme = {self.EPEE1M,
                        self.EPEE2M,
                        self.HACHE1M,
                        self.HACHE2M,
                        self.MARTEAU1M,
                        self.MARTEAU2M,
                        self.LANCE,
                        self.BATON,
                        self.DAGUE,
                        self.ARC,
                        self.ARBALLETTE
                        }
        self.to_print = "Arme ? : "
        self.listdisp = {}
        for i in self.tt_arme:
            if i.OK:
                self.listdisp.__setitem__(i, -1)
                self.to_print += i.NAME + ", "
        print(self.to_print)
        self.OK1 = False
        while not self.OK1:
            self.R = input()
            for i in self.listdisp:
                if self.R == i.NAME:
                    self.OK1 = True
                    self.ARME1 = i
                    self.dualhanded = self.ARME1.MAINS
                    self.listdisp.__delitem__(i)
                    print("OK")
                    break
            if not self.OK1:
                print("huh?")
        self.listdisp.__setitem__(BOUCLIER(),-1)
        self.listtodel = {}
        for i in self.listdisp:
            if i.MAINS:
                self.listtodel.__setitem__(i,-1)
        for i in self.listtodel:
            self.listdisp.__delitem__(i)
        for i in self.listdisp:
            self.to_print += i.NAME + ", "
        self.OK2 = False
        if not self.dualhanded:
            while not self.OK2:
                for a in self.listdisp:
                    self.R = str(input())
                    if self.R == str(a.NAME):
                        self.OK2 = True
                        self.ARME2 = a
                        self.listdisp.__delitem__(a)
                        break
                if not self.OK2:
                    print("huh?")
        else:
            self.ARME2 = EMPTYHAND
        self.DEG = 0
        self.e_a = {self.ARME1, self.ARME2}
        self.LDEG = 4


def interpret(r_input,your_turn):
    if r_input == ("close" or "exit"):
        print("OK")
        exit()
    elif r_input == "present":
        PJ.present()
        print("OK")
    elif r_input == "attaque":
        PJ.attack()
        if your_turn:
            list_to_use = ally_list
        else:
            list_to_use = mob_list
        for i in list_to_use:
            i
        if not your_turn:
            set.ally_list = new_list
        else:
            set.mob_list = new_list
        set.your_turn = False
    elif str.startswith(r_input, "take_a "):
        g_max = int(str.strip(r_input, "take_a "))
        g = 0
        while g <= g_max:
            mob.attack()
            list_to_use = mob_list
            for i in list_to_use:
                i
            set.mob_list = new_list
            g += 1
    else:
        print("huh?")


class BOUCLIER:
    def __init__(self):
        self.NAME = "Bouclier"
        self.DEG = {0, 0, 0}
        self.MAINS = False
        self.MAGIC = True
        self.OK = False


class EMPTYHAND:
    def __init__(self):
        self.ARME = ""
        self.DEG = {0, 0, 0}
        self.MAINS = False
        self.MAGIC = False
        self.OK = False


def you_lose():
    print("you_lose")
    PJ.present()
    exit()


OK1 = False
to_print = "Classe ? : "
for i in CLASSE.liststr:
    to_print = to_print + i + ", "
print(to_print)
while not OK1:
    sub = M.nomag()
    R1 = str(input())
    for i in CLASSE.listfunc:
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
PJ = monperso(classe, race, sub)
PJ.present()
mob = MOB.MOB(PJ)
Turn = 0
your_turn = True
mob.new()
ally_list = {}
mob_list = {}
new_list = {}
while True:
    if PJ.PV <= 0:
        you_lose()
    if mob.PV <= 0:
        mob.die()
    print("?")
    if your_turn:
        interpret(input())
    else:
        mob.attack()
        if your_turn:
            list_to_use = ally_list
        else:
            list_to_use = mob_list
        for i in list_to_use:
            i
        if not your_turn:
            ally_list = new_list
        else:
            mob_list = new_list
        new_list = {}
        your_turn = True
