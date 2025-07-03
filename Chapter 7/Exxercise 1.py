# define a function that takes a number n and returns dictionary containing cubes of that number

def cube_finder(n):
    cubes = {} # dictionary name
    for i in range(1, n + 1): # i means key of a no.
        cubes[i] = i ** 3
    return cubes
print(cube_finder(5))


# taking input from user

# number = int(input("Enter number: "))
# def cube_finder(n):
#     cubes = {} # dictionary name
#     for i in range(1, n + 1): # i means key of a no.
#         cubes[i] = i ** 3
#     return cubes
# print(cube_finder(number))
