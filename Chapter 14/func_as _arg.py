# def square(a):
#     return a ** 2
# l = [3,4,2,6]
# # print(list(map(square,l)))
# def my_map(func,l):
#     new_list = []
#     for item in l:
#         new_list.append(func(item))
#     return new_list
# print(my_map(square,l))




l = [4,5,3,9,2]
def my_map(func,l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list

def my_map2(func,l):
    return [func(item) for item in l]
print(my_map2(lambda x : x ** 3,l))


