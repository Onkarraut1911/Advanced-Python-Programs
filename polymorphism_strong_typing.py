class Duck(object):
    def walk(self):
        print("thapak thapak thapak thapak thapak ")

class Hours(object):
    def walk(self):
        print("tabdak tabdak tabdak tabdak tabdak")

class Cat(object):
    def walk(self):                                           # This is instance method
        print("show show show show show show")
    
    def talk(self):
        print("meow meow meow meow meow meow")

def myfunction(obj):    # this method dont know which type of object its give   , This is function
    if hasattr(obj, 'walk'):   # this function check 'walk' method is have obj or not if it have then return true and run statement
        obj.walk()
    if hasattr(obj , 'talk'):
        print()
        obj.talk()



D = Duck()
myfunction(D)

H = Hours()
myfunction(H)

C = Cat()
myfunction(C)