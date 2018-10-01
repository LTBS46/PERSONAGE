class AIR:
    def __init__(self):
        self.TYPE = "Air"
        self.MANA = 1.1


class EAU:
    def __init__(self):
        self.TYPE = "eau"
        self.MANA = 1.2


class FEU:
    def __init__(self):
        self.TYPE = "feu"
        self.MANA = 1.2


class OMNI:
    def __init__(self):
        self.TYPE = "omni"
        self.MANA = 1.3


class nomag:
    def __init__(self):
        self.TYPE = "nul"
        self.MANA = 1


liststr = {"AIR",
           "EAU",
           "FEU",
           "OMNI"
           }
listfunc = {AIR(),
            EAU(),
            FEU(),
            OMNI()
            }
