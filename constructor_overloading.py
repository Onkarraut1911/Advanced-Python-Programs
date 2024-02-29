class Father(object):
    def __init__(self):
        self.money = 1000
        print("Father class constructor")

    def show(self):
        print("Father class instance method")
    
class Son(Father):
    def __init__(self):   #override the parent constructor
        self.money = 2000
        self.car = 'BMW'
        print("Son class constructor")

    def disp(self):
        print("Son class instance method")

s = Son()