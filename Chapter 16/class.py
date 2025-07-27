class person:
    def __init__(self,firstName, lastName, age):
        #instance variables
        self.first_name = firstName
        self.last_name = lastName
        self.age = age
        self.full_name = firstName + "   " + lastName

# object creation
p1 = person("priti","kharde",24)

# access data through objects

print(p1.first_name)
print(p1.age)
print(p1.full_name)

