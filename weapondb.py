__author__ = 'Paultimate'


class WeaponDB():
    """Here be thine weapons of thy holy might"""

    def __init__(self):
        self.wepdb = {'None'    : "Error: No Weapon stats to get selected.",
                      'Sword'   : ("Sword", 3, 5, 1.5, 2.0),
                      'Sword1'  : ("Sword+1", 4, 6, 1.5, 2.0),
                      'Sword2'  : ("Sword+2", 5, 7, 1.5, 2.0),
                      'Sword3'  : ("Sword+3", 6, 8, 1.5, 2.0),
        }

    def getDBValues(self, key='None'):
        try:
            return self.wepdb[key]
        except KeyError:
            return self.wepdb['None']

    def getItemList(self):
        for key in self.wepdb:
            print self.wepdb[key]


#m = WeaponDB()
#m.getItemList()