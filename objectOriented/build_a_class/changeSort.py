class Foo(object):
    def __init__(self, name):
        """ name is just a string """
        self.name = name

    '''def __lt__(self, other):
        """ I'm curious to see if this will sort in reverse order """
        return self.name > other.name 
'''
    def __gt__(self, other):
        """ This works to reverse sort as well which implies that list
            method sort looks for either of these """
        return self.name < other.name

    def __str__(self):
        return self.name


a = Foo('Young')
b = Foo('Old')
c = Foo('Love')
d = Foo('Tears')
e = Foo('Learn')

objList = [a, b, c, d, e]

for e in objList:
    print(e)

objList.sort()

print("After sorting\n")
for e in objList:
    print(e)
