from functools import wraps
def only_data_type_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper_function(*args, **kwargs):
            if all([type(arg) == data_type for arg in args]):
                return function(*args, **kwargs)
            print("Invalid Arguments")
        return wrapper_function
    return decorator

@only_data_type_allow(str)
def string_join(*args):
    string = " "
    for s in args: 
        string += s
    return string
print(string_join("priti","kharde","be"))
print(string_join("priti","kharde","be",6))