class Person:
    def __init__(self,firstName,lastName,age):
        print("init called")
        self.FN = firstName
        self.LN = lastName
        self.age = age

    # instnce method
    def full_name(self):
        return f"{self.FN} {self.LN}"
    
    # instance method
    def is_above_18(self):
        return self.age>18\
        

p1 = Person("priti",'kharde',31)
print(p1.full_name())

p2 = Person("dvc",'gjcs',16)
print(p2.full_name())

print(p2.is_above_18())
