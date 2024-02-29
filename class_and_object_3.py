class Mobile(object):
    def __init__(self,m):
        self.model = m
    
    def show_model(self,p):
        Price = p 
        print("Model: ",self.model , ",    Price: ",Price)

Realme = Mobile('RealMe X')
Realme.show_model(1000)
print(id(Realme))  # id is the show address of object
print()

samsung = Mobile('samsung')
samsung.show_model(5000)
print(id(samsung))
print()

oppo = Mobile('oppo')
oppo.show_model(3000)
print(id(oppo))
print()


