#check palindrom or not
# def is_palindrom(word):
#     reverse = word[::-1]
#     if word == reverse:
#        return True
#     else:
#         return False
    
# print(is_palindrom("madam"))
# print(is_palindrom("horse"))



#by taking user input
def is_palindrom(word):
    reverse = word[::-1]
    if word == reverse:
        print("It is palindrom")
    else:
        print("not palindrom")

str = input("Enter your string: ")
(is_palindrom(str))


