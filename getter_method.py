class Mobile(object):
    def __init__(self):
        self.model = 'RealMe X'   #instance variable
    
    def get_model(self):     #Accessor method / getter method   
        return self.model
    
realme = Mobile()
m = realme.get_model()      #calling Accessor method
print(m)