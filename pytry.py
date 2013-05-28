
__author__ = 'Paultimate'

from weapon import *


class Main():

    def lolstuff(self):

        #print 15 * 2.22

        Sword = Weapon("Sword", 5, 55, 1.55, 2.1)


        crit = Sword.getDamageCrtRND()
        scrit = Sword.getDamageSCrtRND()
        avg = Sword.getDamageAvg()
        high = Sword.getDamageHigh()
        low = Sword.getDamageLow()
        mod = Sword.getDamageMod()
        norm = Sword.getDamageNrmRND()
        name = Sword.getWeaponName()

        # print "Name: " + name
        # print "-----------"
        # print "High: " + str(high)
        # print "Low : " + str(low)
        # print "Avg : " + str(avg)
        # print "Crit: " + str(crit)

        print "-----------"
        print "Name: " + name
        print "-----------"
        print "High: %s" % high
        print "Low : %s" % low
        print "Avg : %s" % avg
        print "Crit: %s" % crit
        print "--------------------"
        print "Rounded Num: %s" % Sword.getRound(11.11311, 4)