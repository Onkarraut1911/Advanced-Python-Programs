class Mobile(object):
    fp = 'Yes'
    @staticmethod
    def show_model(m , p ):
        model = m
        price = p
        print('fingerprint: ',Mobile.fp)
        print("price:",price , " model: ",model)

realme = Mobile()
Mobile.show_model('RealMe X',5000)