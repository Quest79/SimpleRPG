__author__ = 'Paultimate'


class hero():

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
            "Welcome": "Greetings, hero. What is thine name? ",
            "AskClass": "A fine name, {Name}. What is your class? ",
            "AskWeapon": "A {Class}, hmm? What shalt thy weapon be? ",
        }

    def setHeroDict(self, textkey, herokey):
        n = raw_input(self.herotext[textkey].format(**self.herodict))
        self.herodict[herokey] = n
        print self.herodict[herokey]

    def heroMake(self):
        h = hero("Tommy", "Mage", "Staff")
        h.setHeroDict("Welcome", "Name")
        h.setHeroDict("AskClass", "Class")
        h.setHeroDict("AskWeapon", "Weapon")
#
# print h.herodict["Name"]
# print h.herodict["Class"]
# print h.herodict["Weapon"]