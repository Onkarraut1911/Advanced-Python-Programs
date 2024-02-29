class Mobile(object):
    fp = 'Yes'

    classmethod
    def is_fp(cls):
        print("fingerprint : ",cls.fp)

samsung = Mobile()
oppo = Mobile()
realme = Mobile()

print("class fp : ",Mobile.fp)
print("samsung: ",samsung.fp)
print("oppo: ",oppo.fp)
print("realme: ",realme.fp)

print()

Mobile.fp = 'No'

print("class fp : ",Mobile.fp)
print("samsung: ",samsung.fp)
print("oppo: ",oppo.fp)
print("realme: ",realme.fp)

print()

samsung.fp = 'Not working'

print("class fp : ",Mobile.fp)
print("samsung: ",samsung.fp)
print("oppo: ",oppo.fp)
print("realme: ",realme.fp)
