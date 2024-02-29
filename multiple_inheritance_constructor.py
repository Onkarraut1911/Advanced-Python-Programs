class Father(object):
    def __init__(self):
        super().__init__()                      # calling parent class constructor (object)
        print("Father's class constructor")

    def showF(self):
        print("Father's class instance method")

class Mother(object):                            
    def __init__(self):
        super().__init__()                       # calling parent class constructor (object) but object is access so its goes Father class constructor
        print("Mother's class constructor")

    def showM(self):
        print("Mother's class instance method")
    
class Son(Mother , Father):
    def __init__(self):
        super().__init__()
        print("Son's class constructor")

    def ShowS(self):
        print("Son's class instance method")

S = Son()
