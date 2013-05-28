
__author__ = 'Paultimate'

from weapon import *
from loltxt import *


class Main():

    def weaponDamage(self):

        #print 15 * 2.22

        wep = Weapon("Sword", 5, 55, 1.55, 2.1)
        s = sayThings()

        greet = s.Say()

        self.crit = wep.getDamageCrtRND()
        self.scrit = wep.getDamageSCrtRND()
        self.avg = wep.getDamageAvg()
        self.high = wep.getDamageHigh()
        self.low = wep.getDamageLow()
        self.mod = wep.getDamageMod()
        self.norm = wep.getDamageNrmRND()
        self.name = wep.getWeaponName()



        print greet
        print "-----------"
        print "Name: " + self.name
        print "-----------"
        print "High: %s" % self.high
        print "Low : %s" % self.low
        print "Avg : %s" % self.avg
        print "Crit: %s" % self.crit
        print "--------------------"
        print "Rounded Num: %s" % wep.getRound(11.11311, 4)