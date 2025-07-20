# define a function thaat take any no. f lists containing numbers
#[1,2,3],[4,5,6],[7,8,9]
# return average such a that
#(1+4+7)/3 likewisse

# try to mak this anonymous function in one line using lambda

# def avg_finder(l1,l2):
#     avg = []
#     for pair in zip(l1,l2):
#         avg.append(sum(pair)/len(pair))
#     return avg
# print(avg_finder([10,2,35],[40,5,35]))



# def avg_finder(*args):
#     avg = []
#     for pair in zip(*args):
#         avg.append(sum(pair)/len(pair))
#     return avg
# print(avg_finder([10,2,35],[40,5,35],[22,11,33],[1,1,1]))


result = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(result([44,11,77],[33,66,88],[22,55,99]))