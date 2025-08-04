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
    

    ### main code for CM as constructor #####
    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)

p1 = Person("priit","hbcja",24)
p2 = Person("bcshg","fdgvsa",57)

p3 = Person.from_string('harshit,vashisth,25')
print(p3.first_name)
print(p3.age)