class Person:
    count_instance = 0
    def __init__(self,first_name,last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def count_instances(cls):
        # return f"you have created {cls.count_instance} instances of Person class"
        return f"you have created {cls.count_instance} instances of {cls.__name__} class"

p1 = Person("priit","hbcja",24)
p2 = Person("bcshg","fdgvsa",57)
p2 = Person("bcshg","fdgvsa",57)
p2 = Person("bcshg","fdgvsa",57)
print(Person.count_instances())
# print(p2.count_instances()) # not good way