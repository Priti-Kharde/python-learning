class Phone: # base class / parent class
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
    def make_a_call(self,phone_number):
        return f"calling {phone_number}...."
    
class Smartphone(Phone):  #child class / derived class
    def __init__(self,brand,model_name,price,RAM,internal_memory, rear_camera):
        # way 1
        # create instance variables
        # Phone.__init__(self,brand,model_name,price)

        # way 2 super() method
        super().__init__(brand,model_name,price)


        self.RAM = RAM
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    
# object creation
phone1 = Phone('Nokia','1100',3000)
smartphone1 = Smartphone('OnePlus','5',30000,'6GB','64GB','20mp')
print(phone1.full_name())
print(smartphone1.full_name() + f" and price is {smartphone1._price}")
