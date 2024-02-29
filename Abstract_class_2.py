from abc import ABC , abstractmethod

class DefenceForce(ABC):
    def __init__(self):
        self.id = 101

    @abstractmethod
    def area(self):
        pass

    def gun(self):
        print("Gun = AK47, id =",self.id)
    
class Army(DefenceForce):
    def area(self):
        print("Army Area = Land")

class AirForce(DefenceForce):
    def area(self):
        print("AirForce Area = Sky")

class Nevy(DefenceForce):
    def area(self):
        print("Nevy Area = Sea")

a = Army()
af = AirForce()
n = Nevy()

a.gun()
a.area()
print()

af.gun()
af.area()
print()

n.gun()
n.area()
print()