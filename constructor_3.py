class Mobile(object):
    def __init__(self, m , v = 80): #constructor with parameter
        self.model = m
        self.volumn = v

    def show_model(self ,p):
        price = p   #Local Variable
        print("model: ",self.model, "  and price: ",price)
        print("volumn: ",self.volumn)

# passing argument to constructor
realme = Mobile('RealMe x' , 50)

# Accessing Method from outside class 
realme.show_model(2000)
