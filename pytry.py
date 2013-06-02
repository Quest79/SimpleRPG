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
        self.screen = pygame.display.set_mode((self.width, self.height), 0, 32)
        self.place = "catr.jpg"
        self.running = running
        #pygame.init()

    def fib(self, n):
        x = 0
        for i in range(n+1):
            x += i
            print x

    def start(self):
        self.screen.blit(self.img.renderImg(self.place), (0, 0))

        points=[(20,120),(140,140),(110,30)]
        color=(255,255,0)
        position=(300,176)
        rad=(10)
        clock = pygame.time.Clock()
        while self.running:
            clock.tick(60)
            self.screen.blit(self.img.renderImg(self.place), (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    print 'Quitting...'
                    pygame.quit()
                    sys.exit()
                else:
                    print event
            if rad > 30:
                rad = 1
            else:
                rad += 1
            #self.screen.lock()
            #pygame.draw.rect(self.screen, (255, 0, 0), Rect((100,100),(120,55)))
            pygame.draw.polygon(self.screen, color, points)
            pygame.draw.circle(self.screen, color, position, rad)
            #self.screen.unlock()
            pygame.display.flip()  #You will see a BLANK SCREEN without this

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
        h.heroMake()

        if h.herodict["Class"] == "Mage":
            print "OMG MAGE"
        else:
            print "Error :( "

        # h = hero()
        # h.setHeroName()
        # h.setHeroClass()
        # h.setHeroWeapon()
        #
        # self.getDBItem('Sword'),
        # self.crit = self.wep.getDamageCrtRND()
        # self.scrit = self.wep.getDamageSCrtRND()
        # self.avg = self.wep.getDamageAvg()
        # self.norm = self.wep.getDamageNrmRND()
        #
        # print "-----------"
        # print "Name: " + self.wep.name
        # print "-----------"
        # print "High: %s" % self.wep.high
        # print "Low : %s" % self.wep.low
        # print "Avg : %s" % self.avg
        # print "Crit: %s" % self.crit
        # print "--------------------"
        # print "--------------------"