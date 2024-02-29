class Father(object):
    def __init__(self , m):
        self.money = m
        print("Father's class constructor" , self.money)

    def showF(self):
        print("Father's class instance method")
        
class Son(Father):
    def __init__(self , m):
        super().__init__(m)                  # calling Father's class constructor
        print("Son's class constructor")
    
    def showS(self):
        print("Son's class instance method")

class Grandson(Son):
    def __init__(self , m):
        super().__init__(m)                          # calling Son's class constructor
        print("Grandson's class constructor")

    def showG(self):
        print("Grandson's class instance method")

G = Grandson(1000)
