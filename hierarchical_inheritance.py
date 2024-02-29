class Father(object):
    def showF(self):
        print("Parent's class instance method")

class Son(Father):
    def showS(self):
        print("Son's class instance method")

class Doughter(Father):
    def showD(self):
        print("Doughter's class instance method")

S = Son()
D = Doughter()
D.showD()
D.showF()
print()
S.showF()
S.showS()