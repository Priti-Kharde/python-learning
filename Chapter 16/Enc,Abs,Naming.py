class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = price

    def make_a_call(self,phone_number):
        print(f"calling {phone_number}....")

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    

    ### name mangling ####
phone1 = Phone("nokia",'1176',2400)
print(phone1._price)