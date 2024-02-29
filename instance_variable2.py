class Mobile(object):
    def __init__(self):
        self.model = 'RealMe x'

    def show_model(self):
        print('Model: ',self.model) # if you want to access instance variable under the class then its write with self vaiable

realme = Mobile()  #object creation
print(realme.model) # if you want to access instance variable outside the class then its write with object name
print()

samsung = Mobile()
samsung.model = 'samsung x'   #change the instance variable value for only this object is not change other object
print(samsung.model)
print()

oppo = Mobile()
print(oppo.model)
