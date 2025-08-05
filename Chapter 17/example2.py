class Mobile:
    def __init__(self,name):
        self.name = name


class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError("New mobile should be object of Mobile class")


m1 = Mobile('onePlus 5')
m2 = 'Samsung galaxy s8'
mobStore = MobileStore()
# print(mobStore.mobiles)
mobStore.add_mobile(m1)
print(mobStore.mobiles)