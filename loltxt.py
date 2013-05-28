__author__ = 'Paultimate'


class sayThings():
    def __init__(self):
        self.script = {
        'None': 'ERROR: BAD STRING RETURNED.',
        'Greet': 'This is a humble greeting',
        'Other': 'This is something else entirely!',
        'Something': 'This is something to read',
        }

    def Say(self, key='None'):
        try:
            return self.script[key]
        except KeyError:
            return self.script['None']

    def listKeys(self):
        for contact in self.script:
            print contact, # Note the comma

    def listKeys2(self):
        return self.script.keys()

    def listValues(self):
        return self.script.values()

        #s = sayThings()
        #print s.listKeys2()