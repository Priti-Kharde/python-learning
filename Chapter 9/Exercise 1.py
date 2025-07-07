# define a function that take list of strings
# list containing reverse of every string
# do it using LC
# example
# l = ['abc','tuv','xyz']
# reverse_string(l) ---> ['cba','vut','zyx']

# def reverse_string(l):
#     return [name[::-1] for name in l]
# print(reverse_string(['abc','tuv','xyz']))



# taking user input
strings = input("Enter strings separated by commas: ").split(",")
def reverse_string(l):
    return [name[::-1] for name in l]
print(reverse_string(strings))