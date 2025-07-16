# without EF
# names = ['abc','priti',"xyzsf"]
# pos = 0
# for name in names:
#     print(f"{pos} ---> {name}")
#     pos = pos + 1


# with EF
# names = ['abc','priti',"xyzsf"]
# for i ,pos in enumerate(names):
#     print(f"{pos} ---> {i}")


names = ["priti",'abc',"jdbc"]
def find_pos(l,string_to_search):
    for pos,name in enumerate(l):
        if name == string_to_search:
            return pos
    return -1
print(find_pos(names,"priti"))
print(find_pos(names,'bchd'))
