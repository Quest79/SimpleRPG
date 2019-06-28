__author__ = 'Paultimate'


class Hero():

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

    def setHeroDicts(self, textkey, herokey):
        n = input(self.herotext[textkey].format(**self.herodict))

        if n == "":
            n = self.herodict[herokey]

        self.herodict[herokey] = n
        #print self.herodict[herokey]

    def heroMake(self):
        self.setHeroDicts("Welcome", "Name")
        self.setHeroDicts("AskClass", "Class")
        self.setHeroDicts("AskWeapon", "Weapon")


# print h.herodict["Name"]
# print h.herodict["Class"]
# print h.herodict["Weapon"]