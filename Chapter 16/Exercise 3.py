class Student:
    count_instance = 0  # class variable

    def __init__(self,FN,LN,age):
        Student.count_instance += 1

        self.firstName = FN
        self.last_name = LN
        self.age = age
    

s1 = Student("ABC","khdb",23)
s2 = Student("XYZ",'hjdbc',86)
s2 = Student("XYZ",'hjdbc',86)
print(s1.count_instance)