name = input("Enter your name : ")
# harshit vashisth

temp_var = ""
i = 0

while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1

