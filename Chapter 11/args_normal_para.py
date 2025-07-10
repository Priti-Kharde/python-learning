# def multiply(*args):
#     multi = 1
#     for i in args:
#         multi *= i
#     return multi
# print(multiply(2,3,4))



# def multiply(num,*args):
#     multi = 1
#     print(num)
#     print(args)
#     for i in args:
#         multi *= i
#     return multi
# print(multiply(2,3,4))


def multiply(string1,string2,*args):
    multi = 1
    print(string1)
    for i in args:
        multi *= i
    return multi
print(multiply("p",4,5))
