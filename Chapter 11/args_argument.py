#args as argument
def add(*args):
    summ = 0
    for i in args:
        summ += i
    return summ
num = [10,50,40]
print(add(*num))