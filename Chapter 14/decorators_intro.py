# def decorator_function(any_function): # kontahi function gheil jyachi functionality enhnce karaychi te
#     def wrapper_function():
#         print("this is awesome function") # functionaloty you wanna add print here
#         any_function()
#     return wrapper_function



# def func1():
#     print("this is function1")

# def func2():
#     print("this is function2")

# # var1 = decorator_function(func1)
# # var1() #Wrapper function call

# func1 = decorator_function(func1)
# func1() #Wrapper function call





def decorator_function(any_function): 
    def wrapper_function():
        print("this is awesome function") 
        any_function()
    return wrapper_function


@decorator_function
def func1():
    print("this is function1")

def func2():
    print("this is function2")

func1()