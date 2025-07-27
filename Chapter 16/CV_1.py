class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
        # self.pi = pi

    def circumference(self):
        return 2 * Circle.pi * self.radius
    
c1 = Circle(4)
print(c1.circumference())


#example 2

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
        discount_price = (Laptop.discount_percent/100) * self.price
        return self.price - discount_price


# to make discount 0
Laptop.discount_percent = 0


#objects
laptop1 = Laptop("dell",'i5 core',20000)
laptop2 = Laptop("apple",'mackbook',67400)


print(laptop2.apply_discount())

# to find namepsace
print(laptop1.__dict__)