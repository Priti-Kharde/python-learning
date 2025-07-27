class Laptop:
    def __init__(self,brand,model,price):
        print("init method get called ")
        # instance variables
        self.brand_name = brand
        self.model_name = model
        self.price = price


    def apply_discount(self,num):
        # self.price
        discount_price = (num/100) * self.price
        return self.price - discount_price



# object
laptop1 = Laptop("dell",'i5 core',20000)
laptop2 = Laptop("apple",'mackbook',67400)
print(laptop2.apply_discount(50))