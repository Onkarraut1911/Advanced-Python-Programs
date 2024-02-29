class Mobile(object ):
    fp = 'Yes'

    @classmethod
    def is_fp(cls):
        print("finger print: ",cls.fp)

realme = Mobile()
samsung = Mobile()
oppo = Mobile()

print("RealMe: ",Mobile.fp)
print("Samsung: ",Mobile.fp)
print("Oppo: ",Mobile.fp)
print()

Mobile.fp = 'No'      # Modifying class variable

print("RealMe: ",Mobile.fp)
print("Samsung: ",Mobile.fp)
print("Oppo: ",Mobile.fp)
