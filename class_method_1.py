class Mobile(object):
    fp = 'Samsung'
    @classmethod             # decorator
    def show_model(cls):      # class method
        print("fingerprint: ",cls.fp)
        print("RealMe X")
    
realme = Mobile()
Mobile.show_model()           #calling class method