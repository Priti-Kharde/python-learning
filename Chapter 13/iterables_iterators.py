numbers = [1,2,3,4]  #iterables
squares = map(lambda a : a**2, numbers)  # iterator

# for i in numbers:
#     print(i)

num1_iter = iter(numbers)
print(next(num1_iter))  # gives first item
print(next(num1_iter)) # gives second item
print(next(num1_iter)) # third
print(next(num1_iter)) # fourth

print(next(num1_iter)) # stop iteration

