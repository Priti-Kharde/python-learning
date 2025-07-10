# def total(*args):
#     print(args)
# total(2,5,7,3,10,43)


# add many numbers
def add_total(*args):
    total = 0  # initilally 0
    for i in args:
        total += i
    return total
print(add_total(1,3,4,8))