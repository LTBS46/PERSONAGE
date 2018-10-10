import prefab as p


class ELF:
    def __init__(self):
        self.RACE = "Elf"
        self.PV = 0.95
        self.AC = 1
        self.AL = 1
        self.AH = 0.5
        self.MANA = 8
        self.EPEE1M = True
        self.LANCE = True
        self.BOUCLIER = True
        self.HACHE1M = True
        self.HACHE2M = False
        self.MARTEAU1M = True
        self.MARTEAU2M = False
        self.EPEE2M = True
        self.DAGUE = True
        self.BATON = True
        self.ARC = True
        self.ARBALLETTE = True
        self.ATTFOR = 4
        self.MODFOR = 2
        self.ATTEND = 5
        self.MODEND = 1
        self.ATTDEX = 9
        self.MODDEX = 4
        self.ATTSAG = 7
        self.MODSAG = 3
        self.ATTPER = 5
        self.MODPER = 1


class HUMAIN:
    def __init__(self):
        self.RACE = "Humain"
        self.PV = 1
        self.AC = 1
        self.AL = 1
        self.AH = 1
        self.MANA = 7
        self.EPEE1M = True
        self.LANCE = True
        self.BOUCLIER = True
        self.HACHE1M = True
        self.HACHE2M = True
        self.MARTEAU1M = True
        self.MARTEAU2M = True
        self.EPEE2M = True
        self.DAGUE = True
        self.BATON = True
        self.ARC = True
        self.ARBALLETTE = True
        self.ATTFOR = 6
        self.MODFOR = 2
        self.ATTEND = 6
        self.MODEND = 2
        self.ATTDEX = 6
        self.MODDEX = 2
        self.ATTSAG = 6
        self.MODSAG = 2
        self.ATTPER = 6
        self.MODPER = 3


class MI_ELF:
    def __init__(self):
        self.RACE = "Mi-elf"
        self.PV = 1
        self.AC = 1
        self.AL = 1
        self.AH = 1
        self.MANA = 7.5
        self.EPEE1M = True
        self.LANCE = True
        self.BOUCLIER = True
        self.HACHE1M = True
        self.HACHE2M = True
        self.MARTEAU1M = True
        self.MARTEAU2M = False
        self.EPEE2M = True
        self.DAGUE = True
        self.BATON = True
        self.ARC = True
        self.ARBALLETTE = True
        self.ATTFOR = 4
        self.MODFOR = 2
        self.ATTEND = 5
        self.MODEND = 1
        self.ATTDEX = 9
        self.MODDEX = 4
        self.ATTSAG = 7
        self.MODSAG = 3
        self.ATTPER = 5
        self.MODPER = 1


class MI_NAIN:
    def __init__(self):
        self.RACE = "Mi-nain"
        self.PV = 1.1
        self.AC = 1
        self.AL = 1
        self.AH = 1
        self.MANA = 6.5
        self.EPEE1M = True
        self.LANCE = False
        self.BOUCLIER = True
        self.HACHE1M = True
        self.HACHE2M = True
        self.MARTEAU1M = True
        self.MARTEAU2M = True
        self.EPEE2M = True
        self.DAGUE = True
        self.BATON = True
        self.ARC = True
        self.ARBALLETTE = True
        self.ATTFOR = 6
        self.MODFOR = 2
        self.ATTEND = 7
        self.MODEND = 2
        self.ATTDEX = 6
        self.MODDEX = 2
        self.ATTSAG = 6
        self.MODSAG = 2
        self.ATTPER = 4
        self.MODPER = 2


class MI_ORK:
    def __init__(self):
        self.RACE = "Mi-ork"
        self.PV = 1.15
        self.AC = 1
        self.AL = 1
        self.AH = 1
        self.MANA = 5.5
        self.EPEE1M = True
        self.LANCE = True
        self.BOUCLIER = True
        self.HACHE1M = True
        self.HACHE2M = True
        self.MARTEAU1M = True
        self.MARTEAU2M = True
        self.EPEE2M = True
        self.DAGUE = True
        self.BATON = True
        self.ARC = True
        self.ARBALLETTE = True
        self.ATTFOR = 7
        self.MODFOR = 3
        self.ATTEND = 6
        self.MODEND = 2
        self.ATTDEX = 5
        self.MODDEX = 2
        self.ATTSAG = 5
        self.MODSAG = 1
        self.ATTPER = 5
        self.MODPER = 2


class NAIN:
    def __init__(self):
        self.RACE = "Nain"
        self.PV = 1.15
        self.AC = 1
        self.AL = 1
        self.AH = 1
        self.MANA = 6
        self.EPEE1M = False
        self.LANCE = False
        self.BOUCLIER = True
        self.HACHE1M = True
        self.HACHE2M = True
        self.MARTEAU1M = True
        self.MARTEAU2M = True
        self.EPEE2M = True
        self.DAGUE = True
        self.BATON = True
        self.ARC = True
        self.ARBALLETTE = True
        self.ATTFOR = 7
        self.MODFOR = 3
        self.ATTEND = 8
        self.MODEND = 3
        self.ATTDEX = 6
        self.MODDEX = 2
        self.ATTSAG = 6
        self.MODSAG = 2
        self.ATTPER = 3
        self.MODPER = 1


class ORK:
    def __init__(self):
        self.RACE = "Ork"
        self.PV = 1.3
        self.AC = 0.5
        self.AL = 1
        self.AH = 1
        self.MANA = 4
        self.EPEE1M = True
        self.LANCE = True
        self.BOUCLIER = True
        self.HACHE1M = True
        self.HACHE2M = True
        self.MARTEAU1M = True
        self.MARTEAU2M = True
        self.EPEE2M = True
        self.DAGUE = False
        self.BATON = True
        self.ARC = False
        self.ARBALLETTE = True
        self.ATTFOR = 9
        self.MODFOR = 4
        self.ATTEND = 7
        self.MODEND = 3
        self.ATTDEX = 5
        self.MODDEX = 2
        self.ATTSAG = 4
        self.MODSAG = 1
        self.ATTPER = 5
        self.MODPER = 1

liststr = {"ELF",
           "HUMAIN",
           "ORK",
           "MI_ELF",
           "MI_ORK",
           "MI_NAIN",
           "NAIN"
           }
listfunc = {ELF(),
            HUMAIN(),
            ORK(),
            MI_ELF(),
            MI_ORK(),
            MI_NAIN(),
            NAIN()
            }
