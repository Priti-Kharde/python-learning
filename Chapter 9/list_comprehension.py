# EXAMPLE 1
# squares from 1 to 10 using list
# square = []
# for i in range(1,11):
#     square.append(i ** 2)
# print(square)


# using list Comprehension
# square1 = [i**2 for i in range(1,11)]
# print(square1)


# EXAMPLE 2
# to print negative numbers from 1 to 10
# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)

# using LC
# negative1 = [-i for i in range(1,11)]
# print(negative1)


# EXAMPLE 3
# print first letters of given names
# names =["Priti","Kalyani","Reshma"]
#new_list =["p","K","R"] # output

# in normal list
# names =["Priti","Kalyani","Reshma"]
# new_list =[]
# for name in names:
#     new_list.append(name[0])
# print(new_list)

# using LC
names = ["Priti","Kalyani","Reshma"]
new_list2 = [name[0] for name in names]
print(new_list2)