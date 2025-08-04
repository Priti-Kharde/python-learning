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


class FlagshipPhone(Smartphone):
    def __init__(self,brand,model_name,price,RAM,internal_memory, rear_camera,front_camera):
        super().__init__(brand,model_name,price,RAM,internal_memory, rear_camera)

        self.front_camera = front_camera
    

    
# object creation
phone = Phone('Nokia','1100',5000)
sm = Smartphone('OnePlus','5',30000,'6GB','64GB','20mp')
fs = FlagshipPhone('OnePlus','5',30000,'6GB','64GB','20mp','16MP')
print(isinstance(fs,Smartphone))


