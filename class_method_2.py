class Mobile(object):
    fp = 'Yes'

    @classmethod
    def show_model(cls ,r):
        cls.ram = r
        print('fingerprint : ',cls.fp)
        print("Ram: ",cls.ram)
        
realme = Mobile()
Mobile.show_model('4GB')
