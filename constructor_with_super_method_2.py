class Father(object):
    def __init__(self , m):
        self.money = m
        print("Parent class constructor")

    def show(self):
        print("Parent class instance method")
    
class Son(Father):
    def __init__(self,m , j):
        self.job = j
        super().__init__(m)         #calling parent class constructor
        print("child class constructor")

    def disp(self):
        print("child class instance method" , self.money , " job : ",self.job)
    
s = Son(1000 , 'python')
s.disp()
