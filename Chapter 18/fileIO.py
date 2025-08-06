file = open('file1.txt') # path of file
# print(f"cursor position: {file.tell()}")

# print(file.read())
# print(file.readline())
# print(file.readline(),end = "")
# print(file.readline())

# # print(f"cursor position: {file.tell()}")
# # print("before seek method..")

# # file.seek(0)
# # print("after seek method..")
# # print(f"cursor position: {file.tell()}")
# # print(file.read())

# file.close()



# file = open('file1.txt')
# line = file.readlines()
# print(len(line))
# file.close()


# to view your file name 
# use data descriptors # name , closed
print(file.name)

file.close()
print(file.closed)

