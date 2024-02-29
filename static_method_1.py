class Mobile(object):
    @staticmethod         #decorator
    def show_model():     #static method
        print("RealMe X")
    
realme = Mobile()
Mobile.show_model()   # calling static method