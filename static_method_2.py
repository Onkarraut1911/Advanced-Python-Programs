class Mobile(object):
    fp = 'Yes'
    @staticmethod
    def show_model():
        print("fingerprint : ",Mobile.fp)

realme = Mobile()
Mobile.show_model()