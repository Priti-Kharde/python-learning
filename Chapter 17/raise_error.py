def add(a,b):
    if (type(a) is int and type(b) is int):
        return a + b
    # return "wrong data type"
    raise TypeError("oops..you are passing wrong data type")


print(add('3','4'))