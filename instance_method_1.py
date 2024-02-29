class Mobile(object):

    def __init__(self):
        self.model = 'Samsung J2'  #instance variable    

    def show_model(self): #instance method without parameter
        print("RealMe X")
        print("samsung : ",self.model)

    #instance method with parameter
    def show_price(self,p):   # self variable automaticaly get the parameter from object as current object referance
        self.price = p 
        print("Price: ",self.price)

realme = Mobile()
realme.show_model()
realme.show_price(5000)