# example = [[1,2,3],[1,2,3],[1,2,3]]
# nested = [i for i in range(1,4) for var in range(3)]
# print(nested)

example = [[1,2,3],[1,2,3],[1,2,3]]
nested = [[i for i in range(1,4)] for var in range(3)]
print(nested)