# common elements finder function
#define a functio which take 2 lists as an input and return a list which contains common elements of both lists

# input ----> [1,2,5,8],[7,1,2,6]
#output -----<[1,2]
def common_finder(l1,l2):
    output =[]
    for i in l1:
        if i in l2:
            output.append(i)
    return output

print(common_finder([1,2,5,8],[7,1,2,6]))
