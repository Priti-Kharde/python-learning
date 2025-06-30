# def reverse_list(l):
#     l.reverse()
#     return l

# numbers = [1,2,3,4]
# print(reverse_list(numbers))



def reverse_list(l):
    empty_list = []
    for i in range(len(l)):
        popped_item = l.pop()
        empty_list.append(popped_item)
    return empty_list

numbers = [1,2,3,4]
output_reverse = reverse_list(numbers)
print(output_reverse)


