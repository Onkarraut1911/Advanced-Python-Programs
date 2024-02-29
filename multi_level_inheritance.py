class Father(object):
    def showF(self):
        print("Father's class instance method")

class Son(Father):
    def showS(self):
        print("Son's class instance method")
    
class Grandson(Son):
    def showG(self):
        print("Grandson's class instance method")

G = Grandson()
G.showF()
G.showS()
G.showG()
