class Father(object):
    def __init__(self, m):
        # self.money = 1000
        self.money = m
        print("Father class Constructor")

    def show(self):
        print("Father class Instance method")

class Son(Father):
    def disp(self):
        print("Son class intance method",self.money + 1000)

s = Son(1000)   # creating object of son class and its automaticaly call the parent class constructor
s.show()
print(s.money)
s.disp()

