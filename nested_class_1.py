class Army(object):       #outer class
    def __init__(self):
        self.name = 'Rahul'
        self.gn = self.Gun()  #creating inner class object

    def show(self):
        print("Name: ", self.name)

    class Gun(object):
        def __init__(self):
            self.name = 'AK47'
            self.capacity = '75 Rounds'
            self.length = '34.3 In'

        def disp(self):

            print("Gun Name: ",self.name)
            print("Capacity: ",self.capacity)
            print("Length: ",self.length)

a = Army()
print(a.name)
a.show()

print(a.gn.name)
g = a.gn


Gunobject = Army().Gun()   #creating object of inner class  outside the class
print()

print(g.name)
print(g.capacity)
print(g.length)
print()

g.disp()

print()
print(Gunobject.name)
print(Gunobject.capacity)
print(Gunobject.length)
print()

Gunobject.disp()
