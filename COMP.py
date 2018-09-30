import MAIN


class PEAUDURE:
    def __init__(self):
        self.NAME = "Peau_dure"
        self.TYPE = "PASSIF"


class SOIN:
    def __init__(self):
        self.NAME = "Soin"
        self.TYPE = "ACTIF"


class CHEVAL:
    def __init__(self):
        self.NAME = "Cheval"
        self.TYPE = "PASSIF"


class RESURECITON:
    def __init__(self):
        self.NAME = "Résurection"
        self.TYPE = "ACTIF"


class BOULEDENERGIE:
    def __init__(self):
        self.NAME = "Boule d'énérgie"
        self.TYPE = "ACTIF"


class CONNAISSANCEDEFORET:
    def __init__(self):
        self.NAME = "Connaissance de la forêt"
        self.TYPE = "PASSIF"


class DRAINMANA:
    def __init__(self):
        self.NAME = "Drain de mana"
        self.TYPE = "ACTIF"


class DRAINPV:
    def __init__(self):
        self.NAME = "Drain de vie"
        self.TYPE = "ACTIF"


class COMPAGNON:
    def __init__(self):
        self.NAME = "Drain de vie"
        self.TYPE = "ACTIF"

    def attack(self):
        MAIN.mob.take_damage(MAIN.PJ.LVL*3)
