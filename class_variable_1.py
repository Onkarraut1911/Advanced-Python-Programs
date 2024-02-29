class Mobile(object):
    fp = 'Yes'   #class variable or static variable

    @classmethod
    def is_fp(cls):   #class method
        print(cls.fp)   #Accessing class variable

realme= Mobile()
Mobile.is_fp()   # Access class variable outside the class using class name     