# def is_even(i):
#     return i % 2 == 0
# nums = [5,30,28,11,51]
# print(list(filter(is_even,nums)))

# using lambda

# nums = [5,30,28,11,51]
# print(list(filter(lambda i : i % 2 == 0, nums)))


# using LC
nums = [2,5,3,99,44,21]
new_evens =[i for i in nums if i % 2 == 0]
print(new_evens)