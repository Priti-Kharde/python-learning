# output like tthis   1:1,2:4,3:9
# square = {num : num**2 for num in range(1,11)}
# print(square)

# square = {f" square of{num} is:" : num**2 for num in range(1,11)}
# print(square)


# to count no of times character appears in a string
string = "Priti"
word_count = { char : string.count(char) for char in string}
print(word_count)

