class Father(object):        #parent class     
    money = 1000              # class variable
    def show(self):
        print("Parent class instance method")
    
    @classmethod
    def showmoney(cls):
        print("Parent class class method: ",cls.money)

    @staticmethod
    def stat():
        a = 10
        print("Parent class static method: " , a)

class Son(Father):        # child class inherited from parent class
    def disp(self):
        print("Child class instance method")

s = Son()
s.disp()     # child class method called
s.show()     # perent class method called
s.showmoney()
s.stat()
print()

f = Father()
f.show()
f.showmoney()
f.stat()