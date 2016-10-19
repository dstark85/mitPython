# Person.py
import datetime
''' 
   Shows how a class attribute can be updated 
'''

class Person(object):
    def __init__(self, name):
        """ Create a person called name"""  
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]  # gets the last name

    def getLastName(self):
        """return self's last name """
        return self.lastName

    def setBirthday(self, month, day, year):
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """return True if self's name is lexicographically less than
           other's name, and False otherwise """
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        """ Return self's name """
        return self.name

class MITPerson(Person):
    idnum = 1 # class attribute. Belongs to class. 
    def __init__(self, name):
        Person.__init__(self, name)
        self.id = MITPerson.idnum
        MITPerson.idnum += 1

    def getID(self):
        return self.id

    def __lt__(self, other):
        return self.id < other.id
  
    def speak(self, utterance):
        return (self.getLastName)

me = MITPerson('Derek')
eric = MITPerson('Eric')
bob = Person('Bob')

print(me.getID())
print(eric.getID())
print(me < eric)
