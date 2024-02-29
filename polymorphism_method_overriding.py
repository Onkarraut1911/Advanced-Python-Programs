class Add(object):
    def result(self , a , b):
        print("Addition: ",a+b)

class Multi(Add):
    def result(self , a , b):            # This method is overriding
        super()
        print("Multiplication : ", a*b)

m  = Multi()
m.result(10,20)