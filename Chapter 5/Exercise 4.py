# filter odd even
#define a function
#input is list = [1,2,3,4,5,6,7]
#output ---->[[1,3,5,7],[2,4,6]]


def odd_even(l):
    odd_nums = []
    even_nums = []
    
    for i in l:
        if i % 2 == 0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    
    print("Odd numbers are:", odd_nums)
    
    print("Even numbers are:", even_nums)
    
    return [odd_nums, even_nums]

numbers = [1, 2, 3, 4, 5, 6, 7]
odd_even(numbers) #function call
