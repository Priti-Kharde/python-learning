# odd even
# numbers =[1,2,3,4,5]
# result = []
# for num in numbers:
#     if num % 2 == 0:
#         result.append("Even")
#     else:
#         result.append("odd")
# print(result) 

# by taking User Input
# numbers = input("Enter numbers separated by commas: ").split(",")
# result = []

# for num in numbers:
#     if int(num) % 2 == 0:
#         result.append("Even")
#     else:
#         result.append("Odd")

# print(result)


# using LC
numbers = [2,3,4,5,6]
result = ["even" if i % 2 == 0 else "odd" for i in numbers]
print(result)