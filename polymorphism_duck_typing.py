class Duck(object):
    def walk(self):
        print("thapak thapak thapak thapak thapak ")

class Hours(object):
    def walk(self):
        print("tabdak tabdak tabdak tabdak tabdak")

class Cat(object):
    def walk(self):                                           # This is instance method
        print("show show show show show show")

def myfunction(obj):    # this method dont know which type of object its give   , This is function
    obj.walk()



D = Duck()
myfunction(D)

H = Hours()
myfunction(H)

C = Cat()
myfunction(C)