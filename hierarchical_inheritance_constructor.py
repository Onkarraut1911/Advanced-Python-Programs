class Father(object):
    def __init__(self):
        print("Father's class constructor")

    def showF(self):
        print("Parent's class instance method")

class Son(Father):
    def __init__(self): 
        super().__init__()            # calling Father's class constructor
        print("Son's class constructor")

    def showS(self):
        print("Son's class instance method")

class Doughter(Father):
    def __init__(self):
        super().__init__()            # calling Father's class constructor
        print("Doughter's class constructor")

    def showD(self):
        print("Doughter's class instance method")

S = Son()
D = Doughter()
