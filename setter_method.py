class Mobile(object):
    def __init__(self):
        self.model = 'RealMe X'

    def set_model(self):           # setter method / mutator method
        self.model = 'RealMe 2'
    
realme = Mobile()
#Befor setting
print(realme.model)
#After setting
realme.set_model()        # calling mutator method
print(realme.model)