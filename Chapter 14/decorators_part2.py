# def decorator_function(any_function):
#     def wrapper_function(*args, **kwargs):
#         print("This is awesome function, functionality added")
#         any_function(*args, **kwargs)
#     return wrapper_function

# @decorator_function
# def func(a):
#     print(f"this is function with arguments {a}")

# # func(7) # function call




def decorator_function(any_function):
    def wrapper_function(*args, **kwargs):
        print("This is awesome function, functionality added")
        return any_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def add(a,b):
    return a + b
print(add(3,6))