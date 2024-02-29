class Mobail(object):
    def __init__(self):
        self.model = 'RealMe x'

    def show_model(self):
        print("Model : ",self.model)

RealMe =  Mobail()   # RealMe is the object of Mobail class
RealMe.show_model()
RealMe.model = "RealMe Pro 2"
print(RealMe.model)
RealMe.show_model()