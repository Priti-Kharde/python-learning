################
#greater number between 2 numbers

# def greater_num(a,b):
#     if num1 > num2:
#         return num1
#     return num2

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# bigger = greater_num(num1,num2)

# print(f"{bigger} is greater")



#####################
# Greateest between 3 numbers

def greatest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print("the greatest number is", greatest(num1,num2,num3))