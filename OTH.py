import MAIN

class BOUCLIER:
    def __init__(self):
        self.ARME = "Bouclier"
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


class nomag:
    def __init__(self):
        self.TYPE = "nul"
        self.MANA = 1


class nocomp:
    def __init__(self):
        self.NAME = ""
        self.TYPE = "OTH"


def you_lose():
    print("you_lose")
    MAIN.PJ.present()
    exit()


def autoturn(yours):
    if yours:
        list_to_use = MAIN.ally_list
    else:
        list_to_use = MAIN.mob_list
    for i in list_to_use:
        i
    if yours:
        MAIN.ally_list = MAIN.new_list
    else:
        MAIN.mob_list = MAIN.new_list
    MAIN.new_list = {}