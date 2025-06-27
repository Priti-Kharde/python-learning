# methods to delete data from the list
fruits = ["apple","banana","grapes"]
fruits.pop()  # deletes last element
print(fruits)


fruits = ["apple","banana","grapes"]
fruits.pop(1)  # deletes element on specified postion 
print(fruits)

#del operator
fruits = ["kiwi",'pineapple',"watermelon","papaya"]
del fruits[1]
print(fruits)


# remove() method
fruits = ["apple",'banana',"kiwi","pineapple","banana"]
fruits.remove("banana")
print(fruits)