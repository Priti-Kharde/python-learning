# def word_counter(string):
#     count = {} # empty dictionary
#     for char in string:
#         count[char] = string.count(char) # char is key
#     return count
    
# print(word_counter("priti"))



# take input from user
user_input = input("Enter string: ")
user_input1 = user_input.lower() # counts capital small as same or single character
def word_counter(string):
    count = {} # empty dictionary
    for char in string:
        count[char] = string.count(char) # char is key
    return count
    
print(word_counter(user_input1))