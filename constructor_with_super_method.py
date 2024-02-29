class Father(object):
    def __init__(self):
        print("Parent class constructor")

    def show(self):
        print("Parent class instance method")
    
class Son(Father):
    def __init__(self):
        super().__init__()         #calling parent class constructor
        print("child class constructor")

    def disp(self):
        print("child class instance method")
    
s = Son()
