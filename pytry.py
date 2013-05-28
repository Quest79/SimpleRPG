__author__ = 'Paultimate'

from weapon import *
from loltxt import *


class Main():
    def getDBItem(self, name):
        self.wdb = WeaponDB()
        sword = self.wdb.getDBValues(name)
        self.wep = Weapon(*sword)
        return self.wep

    def weaponDamage(self):
        itemz = [
            self.getDBItem('Sword'),
            self.getDBItem('Sword1'),
            self.getDBItem('Sword2'),
        ]
        for i in itemz:
            s = sayThings()

            greet = s.Say('Greet')

            self.crit = i.getDamageCrtRND()
            self.scrit = i.getDamageSCrtRND()
            self.avg = i.getDamageAvg()
            self.norm = i.getDamageNrmRND()

            print greet
            print "-----------"
            print "Name: " + i.name
            print "-----------"
            print "High: %s" % i.high
            print "Low : %s" % i.low
            print "Avg : %s" % self.avg
            print "Crit: %s" % self.crit
            print "--------------------"
            print "--------------------"