import COMP


class CHASSEUR:
    def __init__(self):
        self.CLASSE = "Chasseur"
        self.PV = 10
        self.MANA = 0.75
        self.ARMOR = "L"
        self.EPEE1M = True
        self.LANCE = False
        self.BOUCLIER = False
        self.HACHE1M = True
        self.HACHE2M = False
        self.MARTEAU1M = False
        self.MARTEAU2M = False
        self.EPEE2M = False
        self.DAGUE = True
        self.BATON = False
        self.ARC = True
        self.ARBALLETTE = True
        self.ATTFOR = 5
        self.MODFOR = 2
        self.ATTEND = 6
        self.MODEND = 2
        self.ATTDEX = 7
        self.MODDEX = 3
        self.ATTSAG = 5
        self.MODSAG = 2
        self.ATTPER = 7
        self.MODPER = 3
        self.COMPBASE1 = COMP.COMPAGNON()
        self.COMPBASE2 = COMP.CONNAISSANCEDEFORET()
        self.COMPBASE3 = COMP.ESQUIVE()
        self.COMPBASE4 = COMP.POISON()


class CHEVALIER:
    def __init__(self):
        self.CLASSE = "Chevalier"
        self.PV = 16
        self.MANA = 1
        self.ARMOR = "H"
        self.EPEE1M = True
        self.LANCE = True
        self.BOUCLIER = True
        self.HACHE1M = True
        self.HACHE2M = True
        self.MARTEAU1M = True
        self.MARTEAU2M = True
        self.EPEE2M = True
        self.DAGUE = False
        self.BATON = False
        self.ARC = False
        self.ARBALLETTE = True
        self.ATTFOR = 7
        self.MODFOR = 3
        self.ATTEND = 7
        self.MODEND = 3
        self.ATTDEX = 7
        self.MODDEX = 3
        self.ATTSAG = 4
        self.MODSAG = 1
        self.ATTPER = 5
        self.MODPER = 2
        self.COMPBASE1 = COMP.CHEVAL()
        self.COMPBASE2 = COMP.PEAUDURE()
        self.COMPBASE3 = COMP.ESQUIVE()
        self.COMPBASE4 = COMP.PLUSGROSPLUSBIEN()


class GUERRIER:
    def __init__(self):
        self.CLASSE = "Guerrier"
        self.PV = 12
        self.MANA = 0.5
        self.ARMOR = "H"
        self.EPEE1M = False
        self.LANCE = True
        self.BOUCLIER = False
        self.HACHE1M = False
        self.HACHE2M = True
        self.MARTEAU1M = False
        self.MARTEAU2M = True
        self.EPEE2M = True
        self.DAGUE = False
        self.BATON = False
        self.ARC = False
        self.ARBALLETTE = False
        self.ATTFOR = 9
        self.MODFOR = 3
        self.ATTEND = 6
        self.MODEND = 2
        self.ATTDEX = 6
        self.MODDEX = 3
        self.ATTSAG = 3
        self.MODSAG = 1
        self.ATTPER = 5
        self.MODPER = 2
        self.COMPBASE1 = COMP.PEAUDURE()
        self.COMPBASE2 = COMP.HEAVYSLASH()
        self.COMPBASE3 = COMP.ESQUIVE()
        self.COMPBASE4 = COMP.MINIMUMFOR()


class MAGE:
    def __init__(self):
        self.CLASSE = "Mage"
        self.PV = 7
        self.MANA = 1.75
        self.ARMOR = "C"
        self.EPEE1M = False
        self.LANCE = False
        self.BOUCLIER = True
        self.HACHE1M = True
        self.HACHE2M = False
        self.MARTEAU1M = False
        self.MARTEAU2M = False
        self.EPEE2M = False
        self.DAGUE = True
        self.BATON = True
        self.ARC = False
        self.ARBALLETTE = False
        self.ATTFOR = 6
        self.MODFOR = 2
        self.ATTEND = 5
        self.MODEND = 2
        self.ATTDEX = 4
        self.MODDEX = 2
        self.ATTSAG = 8
        self.MODSAG = 3
        self.ATTPER = 7
        self.MODPER = 3
        self.COMPBASE1 = COMP.BOULEDENERGIE()
        self.COMPBASE2 = COMP.LANCEFLAMME()
        self.COMPBASE3 = COMP.GEL()
        self.COMPBASE4 = COMP.POISON()


class PALADIN:
    def __init__(self):
        self.CLASSE = "Paladin"
        self.PV = 15
        self.MANA = 1.5
        self.ARMOR = "H"
        self.EPEE1M = True
        self.LANCE = False
        self.BOUCLIER = True
        self.HACHE1M = False
        self.HACHE2M = False
        self.MARTEAU1M = False
        self.MARTEAU2M = True
        self.EPEE2M = True
        self.DAGUE = False
        self.BATON = False
        self.ARC = False
        self.ARBALLETTE = False
        self.ATTFOR = 7
        self.MODFOR = 2
        self.ATTEND = 9
        self.MODEND = 4
        self.ATTDEX = 5
        self.MODDEX = 2
        self.ATTSAG = 7
        self.MODSAG = 3
        self.ATTPER = 3
        self.MODPER = 1
        self.COMPBASE1 = COMP.SOIN()
        self.COMPBASE2 = COMP.PEAUDURE()
        self.COMPBASE3 = COMP.CHEVAL()
        self.COMPBASE4 = COMP.PLUSDARMURE()


class PRETRE:
    def __init__(self):
        self.CLASSE = "Prêtre"
        self.PV = 7
        self.MANA = 1.6
        self.ARMOR = "C"
        self.EPEE1M = False
        self.LANCE = False
        self.BOUCLIER = True
        self.HACHE1M = True
        self.HACHE2M = False
        self.MARTEAU1M = False
        self.MARTEAU2M = False
        self.EPEE2M = False
        self.DAGUE = False
        self.BATON = True
        self.ARC = False
        self.ARBALLETTE = False
        self.ATTFOR = 3
        self.MODFOR = 1
        self.ATTEND = 4
        self.MODEND = 1
        self.ATTDEX = 5
        self.MODDEX = 2
        self.ATTSAG = 9
        self.MODSAG = 4
        self.ATTPER = 8
        self.MODPER = 3
        self.COMPBASE1 = COMP.SOIN()
        self.COMPBASE2 = COMP.BUFFATK()
        self.COMPBASE3 = COMP.BUFFDEF()
        self.COMPBASE4 = COMP.CURE()


class RODEUR:
    def __init__(self):
        self.CLASSE = "Rodeur"
        self.PV = 12
        self.MANA = 0.6
        self.ARMOR = "L"
        self.EPEE1M = True
        self.LANCE = False
        self.BOUCLIER = False
        self.HACHE1M = True
        self.HACHE2M = False
        self.MARTEAU1M = False
        self.MARTEAU2M = False
        self.EPEE2M = True
        self.DAGUE = True
        self.BATON = True
        self.ARC = True
        self.ARBALLETTE = False
        self.ATTFOR = 6
        self.MODFOR = 2
        self.ATTEND = 7
        self.MODEND = 3
        self.ATTDEX = 6
        self.MODDEX = 3
        self.ATTSAG = 3
        self.MODSAG = 1
        self.ATTPER = 8
        self.MODPER = 3
        self.COMPBASE1 = COMP.POISON()
        self.COMPBASE2 = COMP.CONNAISSANCEDEFORET()
        self.COMPBASE3 = COMP.ESQUIVE()
        self.COMPBASE4 = COMP.MINIMUMDEX()


class SORCIER:
    def __init__(self):
        self.CLASSE = "Sorcier"
        self.PV = 7
        self.MANA = 1.6
        self.ARMOR = "L"
        self.EPEE1M = False
        self.LANCE = False
        self.BOUCLIER = False
        self.HACHE1M = True
        self.HACHE2M = True
        self.MARTEAU1M = False
        self.MARTEAU2M = False
        self.EPEE2M = False
        self.DAGUE = False
        self.BATON = True
        self.ARC = False
        self.ARBALLETTE = False
        self.ATTFOR = 3
        self.MODFOR = 1
        self.ATTEND = 6
        self.MODEND = 2
        self.ATTDEX = 4
        self.MODDEX = 2
        self.ATTSAG = 8
        self.MODSAG = 3
        self.ATTPER = 8
        self.MODPER = 3
        self.COMPBASE1 = COMP.BOULEDENERGIE()
        self.COMPBASE2 = COMP.DRAINPV()
        self.COMPBASE3 = COMP.DRAINMANA()
        self.COMPBASE4 = COMP.POISON()


liststr = {"CHASSEUR",
           "CHEVALIER",
           "GUERRIER",
           "MAGE",
           "PALADIN",
           "PRETRE",
           "RODEUR",
           "SORCIER"}
listfunc = {CHASSEUR(),
            CHEVALIER(),
            GUERRIER(),
            MAGE(),
            PALADIN(),
            PRETRE(),
            RODEUR(),
            SORCIER()
            }
