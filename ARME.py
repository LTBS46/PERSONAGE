class EPEE1M:
    def __init__(self):
        self.NAME = "Epée à 1 main"
        self.DEG = {0, 1, 0}
        self.MAINS = False
        self.MAGIC = True
        self.OK = False


class EPEE2M:
    def __init__(self):
        self.NAME = "Epée à 2 mains"
        self.DEG = {0, 0, 1}
        self.MAINS = True
        self.MAGIC = True
        self.OK = False


class HACHE1M:
    def __init__(self):
        self.NAME = "Hache à 1 main"
        self.DEG = {0, 1, 0}
        self.MAINS = False
        self.MAGIC = False
        self.OK = False


class HACHE2M:
    def __init__(self):
        self.NAME = "Hache à 2 mains"
        self.DEG = {1, 1, 0}
        self.MAINS = True
        self.MAGIC = True
        self.OK = False


class MARTEAU2M:
    def __init__(self):
        self.NAME = "Marteau à 2 mains"
        self.DEG = {3, 0, 0}
        self.MAINS = True
        self.MAGIC = True
        self.OK = False


class MARTEAU1M:
    def __init__(self):
        self.NAME = "Marteau à 1 main"
        self.DEG = {1, 0, 0}
        self.MAINS = False
        self.MAGIC = True
        self.OK = False


class LANCE:
    def __init__(self):
        self.NAME = "Lance"
        self.DEG = {0, 0, 1}
        self.MAINS = True
        self.MAGIC = False
        self.OK = False


class DAGUE:
    def __init__(self):
        self.NAME = "Dague"
        self.DEG = {1, 0, 0}
        self.MAINS = False
        self.MAGIC = False
        self.OK = False


class ARC:
    def __init__(self):
        self.NAME = "Arc"
        self.DEG = {0, 1, 0}
        self.MAINS = True
        self.MAGIC = False
        self.OK = False


class BATON:
    def __init__(self):
        self.NAME = "Baton"
        self.DEG = {1, 0, 0}
        self.MAINS = True
        self.MAGIC = True
        self.OK = False


class ARBALLETTE:
    def __init__(self):
        self.NAME = "Arballette"
        self.DEG = {0, 0, 1}
        self.MAINS = True
        self.MAGIC = False
        self.OK = False


liststr = {"EPEE1M",
           "EPEE2M",
           "HACHE1M",
           "HACHE2M",
           "MARTEAU1M",
           "MARTEAU2M",
           "LANCE",
           "BATON",
           "DAGUE",
           "ARC",
           "ARBALLETTE"
           }
listfunc = {EPEE1M(),
            EPEE2M(),
            HACHE1M(),
            HACHE2M(),
            MARTEAU1M(),
            MARTEAU2M(),
            LANCE(),
            BATON(),
            DAGUE(),
            ARC(),
            ARBALLETTE()
            }
