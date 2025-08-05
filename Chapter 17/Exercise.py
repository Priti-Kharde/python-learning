def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError as err:
        # print("you can't divide a number by zero")
        print(err)
    except TypeError as err:
        # print("number must be int or floats")
        print(err)
    else:
        print("unpepected error")

print(divide(10,2))