# # Output
# # l1 = [1,3,5,7]
# # l2 = [2,4,6,8]

# # input
# # [(1,2),(3,4),(5,6),(7,8)]


# l = [(1,2),(3,4),(5,6),(7,8)]
# # print(list(zip(*l)))
# l1, l2 = list(zip(*l))
# print(l1)
# print(l2)
# print(list(l1))
# print(list(l2))




# find greater between 1,2 and 3,4 and so onnnn
l1 = [1,3,5,7]
l2 = [2,4,6,8]
new_list= []
for i in zip(l1,l2):
    new_list.append(max(i))
print(new_list)