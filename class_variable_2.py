#class variable or static variable with class method

class Mobile(object ):
    fp = 'Yes'

    def __init__(self):              #constructor
        self.model = 'RealMe X'     #instance variable

    def show_model(self):            #instance method
        print("model: ",self.model)   #Accessing instance variable

    @classmethod
    def is_fp(cls):                   #class method
        print("finger print : ",cls.fp)  #Accessing class variable


realme = Mobile()
realme.show_model()
Mobile.is_fp()
print()
Mobile.fp = 'No'  # if class variable changed then its change for all object
Mobile.is_fp()
