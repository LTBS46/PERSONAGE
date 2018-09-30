import random as rng
import MAIN


class MOB:
    def __init__(self):
        self.Num = 0
        self.PV = 0
        self.LVL = MAIN.PJ.LVL
        self.PV = self.LVL * 6
        self.DEG = self.LVL * 6
        self.xp = (rng.randrange(1, 100, 1) / 100) * self.LVL

    def new(self):
        self.LVL = MAIN.PJ.LVL
        print("un monstre de niveau : " + str(self.LVL) + " apparait!")
        self.PV = self.LVL * 6
        MAIN.PJ.reset()

    def die(self):
        self.xp = (rng.randrange(1, 100, 1) / 100) * self.LVL
        print("tu gagne : " + str(self.xp) + "xp!")
        MAIN.PJ.gain_xp(self.xp)
        self.new()

    def attack(self):
        self.DEG = self.LVL * 6
        MAIN.PJ.take_damage(self.DEG)
        print("tu prends " + str(self.DEG))

    def take_damage(self, dam):
        self.PV -= dam
