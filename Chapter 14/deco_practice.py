# # @print_function_data
# def add(a,b):
#     '''this function takes two numbers as arguments and return their sum'''
#     return a + b
# print(add(4,5))
# #output should be
# # you are calling add function
# # this function takes two numbers as parameters and return their sum
# # 9


from functools import wraps
def print_function_data(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        print(f"you are calling {function.__name__}()")
        print(function.__doc__) # to print doctring
        return function(*args, **kwargs)
    return wrapper_function


@print_function_data
def add(a,b):
    '''this function takes two numbers as arguments and return their sum'''
    return a + b
print(add(4,5))