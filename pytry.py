__author__ = 'Paultimate'

from weapon import *
from loltxt import *
from weapondb import *


class Main():
	def weaponDamage(self):
		#print 15 * 2.22

		wdb = WeaponDB()
		wepstats = wdb.getWeaponStats('Sword')
		wep = Weapon(*wepstats)
		#wep2 = Weapon("Sword", 5, 55, 1.55, 2.1)

		print wep
		#print wep2

		s = sayThings()

		greet = s.Say()

		self.crit = wep.getDamageCrtRND()
		self.scrit = wep.getDamageSCrtRND()
		self.avg = wep.getDamageAvg()
		self.norm = wep.getDamageNrmRND()

		print greet
		print "-----------"
		print "Name: " + wep.name
		print "-----------"
		print "High: %s" % wep.high
		print "Low : %s" % wep.low
		print "Avg : %s" % self.avg
		print "Crit: %s" % self.crit
		print "--------------------"
		print "Rounded Num: %s" % wep.getRound(11.11311, 4)

		# TODO Make dict of arrays to store weapon and armor info