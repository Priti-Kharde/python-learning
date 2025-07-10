# def user(l,**kwargs):
#     if kwargs.get('reverse_string') == True:
#         return [name[::-1].title() for name in l]
#     else:
#         return [name.title() for name in l]
# names = ["priti","kalyani"]
# print(user(names))




def user(l,**kwargs):
    if kwargs.get('reverse_string') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]
names = ["priti","kalyani"]
print(user(names,reverse_string = True))
    