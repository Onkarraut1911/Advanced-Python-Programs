class Myclass(object):
    def sum(self , a = None , b = None , c = None ):
        if a != None and b != None and c != None : 
            s = a + b + c
        elif a != None and b != None:
            s = a+b
        else:
            s = 'provide at least two numbers'

        # print("First sum method ", s)
        return s
    
    # def sum(self):                    # same method in one class is not possible in python 
    #     print("Second sum method")

obj = Myclass()
print(obj.sum(10,20))
print()
print(obj.sum(10,20,30))
print()
print(obj.sum(10))
print()
print(obj.sum())