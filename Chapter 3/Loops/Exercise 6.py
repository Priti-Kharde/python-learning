#### sum of numbers from 1 to 10 using for loop

# sum = 0
# for i in range(0,11):
#     sum += i
# print(sum)



#by taking user input
num = int(input("Enter number: "))
sum = 0
for i in range(1, num+1):
    sum += i 
print("sum of numbers is: ", sum)
