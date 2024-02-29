class Father(object):
    def showF(self):
        print("Father's class instance method")

class Mother(object):
    def showM(self):
        print("Mother's class instance method")
    
class Son(Mother , Father):
    def ShowS(self):
        print("Son's class instance method")

S = Son()
S.showF()
S.showM()
S.ShowS()