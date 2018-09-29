import CLASSE as C
import RACE as R
import M_TYPE as M
import random as rng
import math
import ARME as A
import OTH


class monperso:
    def __init__(self, classe, race, sub):
        classe.__init__()
        race.__init__()
        self.CLASSE = classe
        self.RACE = race
        self.SUB = sub
        self.LVL = 1
        self.xp_need = math.pow(self.LVL, 2)
        self.xp = 0
        self.PVMAX = classe.PV * race.PV
        self.PV = self.PVMAX
        if classe.CLASSE == "MAGE":
            sub.__init__()
            self.MANAMAX = classe.MANA * race.MANA * sub.MANA
        else:
            self.MANAMAX = classe.MANA * race.MANA
        self.MANA = self.MANAMAX
        if classe.ARMOR == "L":
            self.LIGHT_ARMOR = race.AL * 2
            self.HEAVY_ARMOR = race.AH
            self.CLOTH = race.AC
        if classe.ARMOR == "H":
            self.LIGHT_ARMOR = race.AL
            self.HEAVY_ARMOR = race.AH * 2
            self.CLOTH = race.AC
        if classe.ARMOR == "C":
            self.LIGHT_ARMOR = race.AL
            self.HEAVY_ARMOR = race.AH
            self.CLOTH = race.AC * 2
        self.ATTFOR = classe.ATTFOR + race.ATTFOR
        self.ATTEND = classe.ATTEND + race.ATTEND
        self.TEND = self.ATTEND
        self.ATTDEX = classe.ATTDEX + race.ATTDEX
        self.ATTPER = classe.ATTPER + race.ATTPER
        self.ATTSAG = classe.ATTSAG + race.ATTSAG
        self.MODFOR = classe.MODFOR + race.MODFOR
        self.MODEND = classe.MODEND + race.MODEND
        self.MODDEX = classe.MODDEX + race.MODDEX
        self.MODPER = classe.MODPER + race.MODPER
        self.MODSAG = classe.MODSAG + race.MODSAG
        self.EPEE1M = A.EPEE1M
        self.EPEE1M.OK = classe.EPEE1M and race.EPEE1M
        self.EPEE2M = A.EPEE2M
        self.EPEE2M.OK = classe.EPEE2M and race.EPEE2M
        self.HACHE1M = A.HACHE1M
        self.HACHE1M.OK = classe.HACHE1M and race.HACHE1M
        self.HACHE2M = A.HACHE2M
        self.HACHE2M.OK = classe.HACHE2M and race.HACHE2M
        self.MARTEAU1M = A.MARTEAU1M
        self.MARTEAU1M.OK= classe.MARTEAU1M and race.MARTEAU1M
        self.MARTEAU2M = A.MARTEAU2M
        self.MARTEAU2M.OK = classe.MARTEAU2M and race.MARTEAU2M
        self.LANCE = A.LANCE
        self.LANCE.OK = classe.LANCE and race.LANCE
        self.BOUCLIER = classe.BOUCLIER and race.BOUCLIER
        self.DAGUE = A.DAGUE
        self.DAGUE.OK = classe.DAGUE and race.DAGUE
        self.ARC = A.ARC
        self.ARC.OK = classe.ARC and race.ARC
        self.BATON = A.BATON
        self.BATON.OK = classe.BATON and race.BATON
        self.ARBALLETTE = A.ARBALLETTE
        self.ARBALLETTE.OK = classe.ARBALLETTE and race.ARBALLETTE
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
        to_print = "Arme ? : "
        self.listdisp = {}
        for i in self.tt_arme:
            if i.OK:
                self.listdisp += i
                to_print += i.ARME + ", "
        print(to_print)
        self.OK1 = False
        while not self.OK1:
            for a in self.listdisp:
                self.R = str(input())
                if self.R == str(a.ARME):
                    self.OK1 = True
                    self.ARME1 = a
                    self.dualhanded = self.ARME1.MAINS
                    self.listdisp -= a
                    break
            if not self.OK1:
                print("huh?")
        self.listdisp += OTH.BOULCIER
        for i in self.listdisp:
            if i.MAINS:
                self.listdisp -= i
        for i in self.listdisp:
            to_print += i.ARME + ", "
        self.OK2 = False
        if not self.dualhanded:
            while not self.OK2:
                for a in self.listdisp:
                    self.R = str(input())
                    if self.R == str(a.ARME):
                        self.OK2 = True
                        self.ARME2 = a
                        self.listdisp -= a
                        break
                if not self.OK2:
                    print("huh?")
        else:
            self.ARME2 = OTH.EMPTYHAND

    def recalculer(self):
        self.PVMAX = self.CLASSE.PV * self.RACE.PV
        if self.CLASSE.CLASSE == "MAGE":
            self.SUB.__init__()
            self.MANAMAX = self.CLASSE.MANA * self.RACE.MANA*self.SUB.MANA
        else:
            self.MANAMAX = self.CLASSE.MANA * self.RACE.MANA
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
        self.ATTFOR = self.CLASSE.ATTFOR + self.RACE.ATTFOR
        self.ATTEND = self.CLASSE.ATTEND + self.RACE.ATTEND
        self.ATTDEX = self.CLASSE.ATTDEX + self.RACE.ATTDEX
        self.ATTPER = self.CLASSE.ATTPER + self.RACE.ATTPER
        self.ATTSAG = self.CLASSE.ATTSAG + self.RACE.ATTSAG
        self.MODFOR = self.CLASSE.MODFOR + self.RACE.MODFOR
        self.MODEND = self.CLASSE.MODEND + self.RACE.MODEND
        self.MODDEX = self.CLASSE.MODDEX + self.RACE.MODDEX
        self.MODPER = self.CLASSE.MODPER + self.RACE.MODPER
        self.MODSAG = self.CLASSE.MODSAG + self.RACE.MODSAG
        self.EPEE1M = self.CLASSE.EPEE1M and self.RACE.EPEE1M
        self.EPEE2M = self.CLASSE.EPEE2M and self.RACE.EPEE2M
        self.HACHE1M = self.CLASSE.HACHE1M and self.RACE.HACHE1M
        self.HACHE2M = self.CLASSE.HACHE2M and self.RACE.HACHE2M
        self.MARTEAU1M = self.CLASSE.MARTEAU1M and self.RACE.MARTEAU1M
        self.MARTEAU2M = self.CLASSE.MARTEAU2M and self.RACE.MARTEAU2M
        self.LANCE = self.CLASSE.LANCE and self.RACE.LANCE
        self.BOUCLIER = self.CLASSE.BOUCLIER and self.RACE.BOUCLIER
        self.DAGUE = self.CLASSE.DAGUE and self.RACE.DAGUE
        self.ARC = self.CLASSE.ARC and self.RACE.ARC
        self.BATON = self.CLASSE.BATON and self.RACE.BATON
        self.ARBALLETTE = self.CLASSE.ARBALLETTE and self.RACE.ARBALLETTE

    def present(self):
        print("|--------------------------------------|")
        if self.SUB == "nul":
            to_print = "|Classe : " + self.CLASSE.CLASSE
            if not self.CLASSE.CLASSE == "Chevalier":
                if (self.CLASSE.CLASSE == "Rodeur") or (self.CLASSE.CLASSE == "Prêtre"):
                    to_print = to_print + "   "
                elif (self.CLASSE.CLASSE == "Paladin") or (self.CLASSE.CLASSE == "Sorcier"):
                    to_print = to_print + "  "
                else:
                    to_print = to_print + " "
            to_print = to_print + "      "
        else:
            if self.SUB.TYPE == "OMNI":
                to_print = "|Classe : " + self.CLASSE.CLASSE + " de " + self.SUB.TYPE
                to_print = to_print + "  "
            else:
                to_print = "|Classe : " + self.CLASSE.CLASSE + " de " + self.SUB.TYPE
                to_print = to_print + "   "
        if not self.RACE.RACE == "Mi-nain":
            if (self.RACE.RACE == "Ork") or (self.RACE.RACE == "Elf"):
                to_print = to_print + "    "
            elif self.RACE.RACE == "Nain":
                to_print = to_print + "   "
            else:
                to_print = to_print + " "
        to_print = to_print + "Race : " + self.RACE.RACE + "|"
        print(to_print)
        to_print = "|Niv : " + str(int(self.LVL))
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
                to_print = to_print + " "
                i += 1
        else:
            while not i == int(space_at_time + 1):
                to_print = to_print + " "
                i += 1
        to_print = to_print + "PV : " + str(int(self.PV)) + "/" + str(int(self.PVMAX))
        i = 0
        while not i == int(space_at_time):
            to_print = to_print + " "
            i += 1
        to_print += "MANA : " + str(int(self.MANA)) + "/" + str(int(self.MANAMAX)) + "|"
        print(to_print)
        to_print = "|XP : " + str(float.__round__(float(self.xp), 2)) + "/" + str(float.__round__(self.xp_need, 0))
        i = 5
        while not self.xp >= math.pow(10, i):
            if i == 0:
                i = -2
            else:
                to_print += " "
            i -= 1
        i = 5
        while not self.xp >= math.pow(10, i):
            if i == 0:
                i = 0
            else:
                to_print += " "
            i -= 1
        to_print += "|"
        print(to_print)
        print("|--------------------------------------|")
        print("|Attributs :                           |")
        to_print = "|FOR : "
        to_print += str(self.ATTFOR)
        if self.ATTFOR < 10:
            to_print += " "
        to_print += " MOD : "
        to_print += str(self.MODFOR)
        to_print += "      END : "
        to_print += str(self.ATTEND)
        if self.ATTEND < 10:
            to_print += " "
        to_print += " MOD : "
        to_print += str(self.MODEND)
        to_print += "|"
        print(to_print)
        to_print = "|DEX : "
        to_print += str(self.ATTDEX)
        if self.ATTDEX < 10:
            to_print += " "
        to_print += " MOD : "
        to_print += str(self.MODDEX)
        to_print += "      PER : "
        to_print += str(self.ATTPER)
        if self.ATTPER < 10:
            to_print += " "
        to_print += " MOD : "
        to_print += str(self.MODPER)
        to_print += "|"
        print(to_print)
        to_print = "|SAG : "
        to_print += str(self.ATTSAG)
        if self.ATTSAG < 10:
            to_print += " "
        to_print += " MOD : "
        to_print += str(self.MODSAG)
        to_print += "                      |"
        print(to_print)
        print("|--------------------------------------|")
        to_print = "|Epée à 1 main : "
        if self.EPEE1M:
            to_print += "OUI"
        else:
            to_print += "NON"
        to_print += "   Arballette : "
        if self.ARBALLETTE:
            to_print += "OUI"
        else:
            to_print += "NON"
        to_print += "|"
        print(to_print)
        to_print = "|Epée à 2 mains : "
        if self.EPEE2M:
            to_print += "OUI"
        else:
            to_print += "NON"
        to_print += "    Bouclier : "
        if self.BOUCLIER:
            to_print += "OUI"
        else:
            to_print += "NON"
        to_print += "|"
        print(to_print)
        to_print = "|Hache à 1 main : "
        if self.HACHE1M:
            to_print += "OUI"
        else:
            to_print += "NON"
        to_print += "       Dague : "
        if self.DAGUE:
            to_print += "OUI"
        else:
            to_print += "NON"
        to_print += "|"
        print(to_print)
        to_print = "|Hache à 2 mains : "
        if self.HACHE2M:
            to_print += "OUI"
        else:
            to_print += "NON"
        to_print += "      Baton : "
        if self.BATON:
            to_print += "OUI"
        else:
            to_print += "NON"
        to_print += "|"
        print(to_print)
        to_print = "|Marteau à 1 main : "
        if self.MARTEAU1M:
            to_print += "OUI"
        else:
            to_print += "NON"
        to_print += "       Arc : "
        if self.ARC:
            to_print += "OUI"
        else:
            to_print += "NON"
        to_print += "|"
        print(to_print)
        to_print = "|Marteau à 2 mains : "
        if self.MARTEAU2M:
            to_print += "OUI"
        else:
            to_print += "NON"
        to_print += "    Lance : "
        if self.LANCE:
            to_print += "OUI"
        else:
            to_print += "NON"
        to_print += "|"
        print(to_print)
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

    def attack(self):
        self.DEG = 0
        self.LDEG = 4
        for i in self.ARME1.DEG:
            self.DEG += rng.randrange(1, self.LDEG) * i
            self.LDEG += 2
        self.LDEG = 4
        for i in self.ARME2.DEG:
            self.DEG += rng.randrange(1, self.LDEG) * i
            self.LDEG += 2
        mob.take_damage(self.DEG)

class MOB:
    def __init__(self):
        self.Num = 0
        self.PV = 0
        self.LVL = PJ.LVL
        self.PV = self.LVL * 6
        self.DEG = self.LVL * 6
        self.xp = (rng.randrange(1, 100, 1) / 100) * self.LVL

    def new(self):
        self.LVL = PJ.LVL
        print("un monstre de niveau : " + str(self.LVL) + " apparait!")
        self.PV = self.LVL*6
        PJ.reset()

    def die(self):
        self.xp = (rng.randrange(1, 100, 1) / 100) * self.LVL
        print("tu gagne : " + str(self.xp) + "xp!")
        PJ.gain_xp(self.xp)
        self.new()

    def attack(self):
        self.DEG = self.LVL * 6
        PJ.take_damage(self.DEG)
        print("tu prends " + str(self.DEG))

    def take_damage(self, dam):
        self.PV -= dam


def interpret(r_input):
    if r_input == ("close" or "exit"):
        print("OK")
        exit()
    elif r_input == "present":
        PJ.present()
        print("OK")
    elif r_input == "attaque":
        PJ.attack()
        Your_turn = False
    elif str.startswith(r_input, "take_a "):
        i_max = int(str.strip(r_input, "take_a "))
        i = 0
        while i <= i_max:
            mob.attack()
            i += 1
    else:
        print("huh?")


def you_lose():
    print("you_lose")
    PJ.present()
    exit()


OK1 = False
print("Classe ? : PALADIN, GUERRIER, CHASSEUR, RODEUR, PRETRE, SORCIER, MAGE, CHEVALIER")
while not OK1:
    sub = "nul"
    R1 = str(input())
    if R1 == "PALADIN":
        classe = C.PALADIN()
        OK1 = True
    elif R1 == "GUERRIER":
        classe = C.GUERRIER()
        OK1 = True
    elif R1 == "CHASSEUR":
        classe = C.CHASSEUR()
        OK1 = True
    elif R1 == "RODEUR":
        classe = C.RODEUR()
        OK1 = True
    elif R1 == "PRETRE":
        classe = C.PRETRE()
        OK1 = True
    elif R1 == "SORCIER":
        classe = C.SORCIER()
        OK1 = True
    elif R1 == "MAGE":
        classe = C.MAGE()
        print("OK")
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
    elif R1 == "CHEVALIER":
        classe = C.CHEVALIER()
        OK1 = True
    else:
        print("huh?")
print("OK")
to_print = "Race ? : "
for s in R.liststr:
    to_print += s + ", "
print(to_print)
OK2 = False
while not OK2:
    R3 = str(input())
    if R3 == "HUMAIN":
        race = R.HUMAIN()
        OK2 = True
    elif R3 == "NAIN":
        race = R.NAIN()
        OK2 = True
    elif R3 == "ELF":
        race = R.ELF()
        OK2 = True
    elif R3 == "ORK":
        race = R.ORK()
        OK2 = True
    elif R3 == "MI_ELF":
        race = R.MI_ELF()
        OK2 = True
    elif R3 == "MI_ORK":
        race = R.MI_ORK()
        OK2 = True
    elif R3 == "MI_NAIN":
        race = R.MI_NAIN()
        OK2 = True
    else:
        print("huh?")
print("OK")
PJ = monperso(classe, race, sub)
PJ.present()
mob = MOB()
Turn = 0
Your_turn = True
mob.new()
while True:
    if PJ.PV <= 0:
        you_lose()
    if mob.PV <= 0:
        mob.die()
    print("?")
    if Your_turn:
        interpret(input())
    else:
        mob.attack()
        Your_turn = True
