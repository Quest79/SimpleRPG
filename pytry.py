__author__ = 'Paultimate'

import sys

from pygame import *
from weapon import *
from imghndler import *
from hero import *


class Main():
    def __init__(self, width=640, height=480, running=True):
        self.width = width
        self.height = height
        self.img = imgHandlr()
        #self.screen = pygame.display.set_mode((self.width, self.height), 0, 32)
        #self.place = "catr.jpg"
        #self.running = running
        #pygame.init()


    def fib(self, n):
        print 'n =', n
        if n > 1:
            return n * n - 1
        else:
            print 'end of the line'
            return 1

    def start(self):
        self.screen.blit(self.img.renderImg(self.place), (0, 0))

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    print 'Quitting...'
                    pygame.quit()
                    sys.exit()
                else:
                    print event

            pygame.display.update()  #You will see a BLANK SCREEN without this


    def getDBItem(self, name):
        self.wdb = WeaponDB()
        sword = self.wdb.getDBValues(name)
        self.wep = Weapon(*sword)
        return self.wep

    def weaponDamage(self):

        # hname = raw_input("Greetings, hero. What is thine name? ")
        # hclss = raw_input("Welcome %s. What is thine class? " % hname)
        # woots = raw_input("Do tell hero %s, whome with teachings of the %s; what shalt your weapon be? " % (hname, hclss))

        h = hero()
        h.setHeroName()


        self.getDBItem('Sword'),
        self.crit = self.wep.getDamageCrtRND()
        self.scrit = self.wep.getDamageSCrtRND()
        self.avg = self.wep.getDamageAvg()
        self.norm = self.wep.getDamageNrmRND()

        print "-----------"
        print "Name: " + self.wep.name
        print "-----------"
        print "High: %s" % self.wep.high
        print "Low : %s" % self.wep.low
        print "Avg : %s" % self.avg
        print "Crit: %s" % self.crit
        print "--------------------"
        print "--------------------"