class Laptop:
    def __init__(self,brand,model,price):
        print("init method get called ")
        # instance variables
        self.brand_name = brand
        self.model_name = model
        self.price = price
# object
laptop1 = Laptop("dell",'i5 core',20000)
laptop2 = Laptop("hp",'i3 core',600000)

print(laptop1.price)