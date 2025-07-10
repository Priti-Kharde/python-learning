# kwargs as a parameter
# def func(**kwargs):
#     print(kwargs)
# func(first="priti", last="kharde")


def func(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(f"{k} : {v}")
func(first="priti", last="kharde")