# fromkeys() method
# keys = ["a","b","cd"]
# new = dict.fromkeys(keys)
# print(new)

# user_info = {
#     'name': "priti",
#     'age' : 24,
#     'city': "pune"
# }
# new = dict.fromkeys(['name','age'],'unknown')
# print(new)
# print(user_info)


# user_info = {
#     'name': "priti",
#     'age' : 24,
#     'city': "pune"
# }
# new = dict.fromkeys(['name','age'],['unknown','25'])
# print(new)



# get() method
# user_info = {
#     'name': "priti",
#     'age' : 24,
#     'city': "pune"
# }
# # print(user_info.get("name"))
# print(user_info.get("namess"))



# clear() method
# user_info = {
#     'name': "priti",
#     'age' : 24,
#     'city': "pune"
# }
# user_info.clear()
# print(user_info)


#copy() method
user_info = {
    'name': "priti",
    'age' : 24,
    'city': "pune"
}
new = user_info.copy()
print(new)