__author__ = 'Paultimate'


class hero():
    """Lets do some heros shit"""

    def __init__(self, name="Jimmy", prof="Warrior", weapon="Sword"):
        """Constructor for hero"""
        self.name = name
        self.prof = prof
        self.weapon = weapon
        self.herodict = {
            "Name": self.name,
            "Class": self.prof,
            "Weapon": self.weapon
        }
        self.herotext = {
            "Welcome": lambda self: "Greetings, hero. What is thine name? ",
            "AskClass": lambda self: "A fine name %s. What is your class? " % self.herodict['Name'],
            "AskWeapon": lambda self: "A %s ? What shalt thy weapon be? " % self.herodict['Class'],
        }

    def thingy(self, textkey, herokey):
        while herokey == "" or self.herodict['Name']:
            n = raw_input(self.herotext[textkey](self))
            self.herodict[herokey] = n

            if self.herodict[herokey] != "":
                print self.herodict[herokey]
            else:
                print "Hero needs a info badly"


    def setHeroName(self):
        self.thingy("Welcome", 'Name')
        # n = raw_input("Greetings, hero. What is thine name? ")
        # self.herodict['Name'] = n
        #
        # if self.herodict['Name'] != "":
        #     print self.herodict['Name']
        # else:
        #     self.herodict['Name'] = self.name
        #     print self.herodict['Name']


    def setHeroClass(self):
        self.thingy("AskClass", "Class")
        # n = raw_input("A fine name %s. What is your class? " % self.herodict['Name'])
        # self.herodict['Class'] = n
        #
        # if self.herodict['Class'] != "":
        #     print self.herodict['Class']
        # else:
        #     self.herodict['Class'] = self.prof
        #     print self.herodict['Class']

    def setHeroWeapon(self):
        self.thingy("AskWeapon", 'Weapon')
        # n = raw_input("A %s ? What shalt thy weapon be? " % self.herodict['Class'])
        # self.herodict['Weapon'] = n
        #
        # if self.herodict['Weapon'] != "":
        #     print self.herodict['Weapon']
        # else:
        #     self.herodict['Weapon'] = self.weapon
        #     print self.herodict['Weapon']


# h = hero()
# h.setHeroName()
# h.setHeroClass()
# h.setHeroWeapon()