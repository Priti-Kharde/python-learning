#ask user a number like 1256
#calculate sum of digits ---> 1+2+5+6


#logic
#num = "1256"  length = 4
#int(num[0])--->1
#int(num[1])--->2
#int(num[2])--->5
#int(num[3])--->6
# i ---> 0 to 3

num = input("Enter number: ")
sum = 0

for i in range(0,len(num)):
    sum += int(num[i])

print("sum of numbers is:", sum)  
