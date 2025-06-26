# if elif else statement


age = int(input("Enter your age: "))
if 0<age<=3:
    print("Ticket is free")
elif 4<age<=10:
    print("Ticket price : 150")
elif 11<age<=60:
    print("Ticket price : 250")
else:
    print("Ticket price : 200")
    