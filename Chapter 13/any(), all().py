num1 = [2,4,6,9,10]
num2 = [1,3,5,7,9]

# evens1 = []
# for num in num1:
#     evens1.append(num % 2 == 0)

# print(evens1)
# print(all([True, True, True, True, True]))

# using list comprehension and all() function
# print(all([num % 2 == 0 for num in num1]))


 # any()  function
print(any([num % 2 == 0 for num in num2]))