class A:
    def show_A(self):
        return 'class A method..'

    def hello(self):
        return "HEllo i am from class A"
    
class B:
    def show_B(self):
        return 'class B method..'

    def hello(self):
        return "HEllo i am from class B"
    
class C(A,B):
    pass

obj_C = C()
print(obj_C.show_A())
print(obj_C.show_B())
print(obj_C.hello())

# MRO
# print(help(C))