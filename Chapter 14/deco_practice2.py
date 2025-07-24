# from functools import wraps
# def only_int_allow(function):
#     @wraps(function)
#     def wrapper_function(*args,**kwargs):
#         data_types =[]
#         for arg in args:
#             data_types.append(type(arg) == int)
#         if all(data_types):
#             return function(*args, **kwargs)
#         else:
#             print("Invalid arguments")

#     return wrapper_function

# @only_int_allow
# def add_all(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total

# print(add_all(1,2,3,4,5))  
# print(add_all(24,666,[76,9,23]))    


from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrapper_function(*args,**kwargs):
        if all([type(arg) == int for arg in args]):
            return function(*args, **kwargs)
        print("Invalid Arguments")
    return wrapper_function

@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add_all(10,2,39,2,5))
print(add_all("2")) 
print(add_all(24,666,[76,9,23]))    

