# def nums(n):
#     for i in range(1,n + 1):
#         print(i)
# nums(10)      

def nums(n):
    for i in range(1,n + 1):
        yield i
print(nums(10))    