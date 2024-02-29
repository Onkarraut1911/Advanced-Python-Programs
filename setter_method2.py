class Mobile(object):
    def set_model(self , m):       # mutator method / setter method
        self.model = m

realme = Mobile()
realme.set_model('RealMe X')  # calling mutator method
print(realme.model)