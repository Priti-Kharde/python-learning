# normal list to print even numbers
# numbers = list(range(1,11))
# nums = []
# for i in numbers:
#     if i % 2 == 0:
#         nums.append(i)
# print(nums)


# using LC
# numbers = list(range(1,11))
# even_nums = [i for i in numbers if i % 2 == 0]
# print(even_nums)

#lc without taking list og numbers
even_nums2 = [i for i in range(1,11) if i % 2 == 0]
print(even_nums2)