#define a function that take list of words as an arg and return list with reverse of every element in that list.

# example ['abc','xyz'] ---->['cba','zyx']

# def reverse_elements(l):
#     elements = []
#     for i in l:
#         elements.append(i[::-1])
#     return elements
    
# words = ['abc','xyz']
# print(reverse_elements(words))


words = input("Enter words separated by comma: ").split(",")
def reverse_elements(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements
print(reverse_elements(words))
