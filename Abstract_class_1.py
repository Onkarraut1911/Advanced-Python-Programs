from abc import ABC , abstractmethod
class Father(ABC):  # can't create object of Abstract class
    @abstractmethod
    def disp(self):
        pass
    
    def show(self):
        print("Concrete Method")

class Child(Father):
    def disp(self):            # if abstract method definition is not write in child class then child class make abstract is compulsory
        print("Child Class")
        print("Defining Abstract Method")

c = Child()
c.disp()
c.show()