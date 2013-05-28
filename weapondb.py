__author__ = 'Paultimate'


class WeaponDB():
    """Here be thine weapons of thy holy might"""

    def __init__(self):
        self.script = {
        'None': "Error: No Weapon stats to get selected.",
        'Sword': ("Sword", 1, 2, 1.5, 2.0),
        'Sword1': ("Sword +1", 2, 3, 1.5, 2.0),
        'Sword2': ("Sword +2", 3, 4, 1.5, 2.0),
        }

    def getWeaponStats(self, key='None'):
        try:
            return self.script[key]
        except KeyError:
            return self.script['None']


            #s = WeaponDB()
            #print s.getWeaponStats('Sword')