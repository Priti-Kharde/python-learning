class Person:
    def __init__(self,first,last,age):
        self.first_name = first
        self.last_name = last
        self.age = age
        
    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)
    
    @classmethod
    def count_instances(cls):
        return f"you have created {cls.count_instance} instances of {cls.__name__}"
    

    ### main code #####
    @staticmethod
    def hello():
        print("this is static method")


    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
p1 = Person("priti",'kharde',24)
p2 = Person("kalyani",'yewale',71)
Person.hello()
    
    

        