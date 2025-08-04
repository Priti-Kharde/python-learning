class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model_name = model
        self.price = price

    def phone_name(self):
        return f"{self.brand} {self.model_name}"
     

    # str , repr
    def __str__(self):
        return f"{self.brand} {self.model_name}"
    
    def __repr__(self):
        return f"{self.brand} {self.model_name} {self.price}"
    

p1 = Phone('Nokia','1100',5000)
print(p1)

print(str(p1))
print(repr(p1))