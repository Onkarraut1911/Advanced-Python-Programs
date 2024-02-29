class Mobile(object):
    def __init__(self):
        self.model = 'RealMe X'  # instance variable

    def show_model(self):
        print(self.model)  # Accessing instance variable

realme = Mobile()

print(realme.model)