from abc import ABC , abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass

    @abstractmethod
    def disp2(self):
        pass

class Child(Father):                     # can't create  object of child class because not defined disp2 method definition 
    def disp(self):
        print("Child class")
        print("Definig Abstract Method")

class GrandChild(Child):
    def disp2(self):
        print("GrandChild class")
        print("Disp2 Abstract Method")

c = GrandChild()
c.disp()
print()
c.disp2()