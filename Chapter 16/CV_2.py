class Laptop:
    discount_percent = 10
    def __init__(self,brand,model,price):
        print("init method get called ")
        # instance variables
        self.brand_name = brand
        self.model_name = model
        self.price = price


    def apply_discount(self):
        # self.price
        discount_price = (self.discount_percent/100) * self.price
        return self.price - discount_price



#objects
laptop1 = Laptop("dell",'i5 core',20000)
laptop2 = Laptop("apple",'mackbook',230000)

# special offer on particular laptop
laptop2.discount_percent = 50
print(laptop2.__dict__)
print(laptop2.apply_discount())



