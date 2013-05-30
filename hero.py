__author__ = 'Paultimate'


class hero():
    """Lets do some heros shit"""

    def __init__(self, name="Jimmy", prof="Warrior", weapon="Sword"):
        """Constructor for hero"""
        self.name = name
        self.prof = prof
        self.weapon = weapon
        self.herodict = {"Name": self.name,
                         "Class": self.prof,
                         "Weapon": self.weapon
        }

    def setHeroName(self):
        n = raw_input("Greetings, hero. What is thine name? ")
        self.herodict['Name'] = n

        if self.herodict['Name'] != "":
            print self.herodict['Name']
        else:
            self.herodict['Name'] = self.name
            print self.herodict['Name']


    def setHeroClass(self, name):
        pass

    def setHeroWeapon(self, name):
        pass


# h = hero()
# h.setHeroName()