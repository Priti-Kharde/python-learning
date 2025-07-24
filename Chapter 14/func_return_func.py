# def outer_f():
#     def inner_f():
#         print("inside inner function")
#     return inner_f
# x = outer_f()
# x()


def outer_f2(msg):
    def inner_f2():
        print(f"message is: {msg}")
    return inner_f2
var = outer_f2("Hello , preeta !!")
var() # to execute inner f2

