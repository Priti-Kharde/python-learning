def power(num, *args):
    if args: #true if not empty ,means args are there
        return [i**num for i in args]
    else:
        return "you didn't pass any args"
# num_list = [4,5,2]
# print(power(2,*num_list))
print(power(2,*[4,5,3]))