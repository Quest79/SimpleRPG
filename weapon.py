__author__ = 'Paultimate'

from rng import *


class Weapon():
    def __init__(self, name="Stick", high=1, low=0, critMod=1, scritMod=2):
        self.rng = randNum()
        self.name = name
        self.high = high
        self.low = low
        self.critMod = critMod
        self.scritMod = scritMod

    def getDamageAvg(self):
        self.avg = (self.high + self.low) / 2.0
        return self.avg

    def getDamageNrmRND(self):
        self.normRND = self.rng.getRandNum(self.high, self.low)
        return self.getRound(self.normRND, 1)

    def getDamageCrtRND(self):
        self.critRND = self.critMod * self.rng.getRandNum(self.high, self.low)
        return self.getRound(self.critRND, 1)

    def getDamageSCrtRND(self):
        self.ScritRND = self.scritMod * self.rng.getRandNum(self.high, self.low)
        return self.getRound(self.ScritRND, 1)

    def getRound(self, num, dec):
        self.rounded = round(num, dec)
        return self.rounded