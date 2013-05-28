__author__ = 'Paultimate'

from rng import *
import math

class Weapon():

    def __init__(self, name, high, low, critMod, scritMod):
        self.rn = randNum()
        self.name = name
        self.high = high
        self.low = low
        self.critMod = critMod
        self.scritMod = scritMod


    def getWeaponName(self):
        return self.name

    def getDamageHigh(self):
        return self.high

    def getDamageLow(self):
        return self.low

    def getDamageMod(self):
        return self.critMod

    def getDamageSMod(self):
        return self.scritMod

    def getDamageAvg(self):
        self.avg = (self.high+self.low)/2.0
        return self.avg

    def getDamageNrmRND(self):
        self.normRND = self.rn.getRandNum(self.high, self.low)
        return self.getRound(self.normRND, 1)

    def getDamageCrtRND(self):
        self.critRND = self.critMod * self.rn.getRandNum(self.high, self.low)
        return self.getRound(self.critRND, 1)

    def getDamageSCrtRND(self):
        self.ScritRND = self.scritMod * self.rn.getRandNum(self.high, self.low)
        return self.getRound(self.ScritRND, 1)

    def getRound(self, num, dec):
        self.rounded = round(num, dec)
        return self.rounded