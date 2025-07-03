# output 
# user_info = {
#     'name' : 'priti',
#    'age' : 24,
#    'fav_movies' : ["ss",'psp',"JK"]
#     'fav_songs' : ['song1','song2']
# }


user = {} # empty D
name = input("Enter your name : ")
age = input("Enter your age : ")
fav_movies = input("Enter movies separated by comma: ").split(",")
fav_songs = input("Enter songs separated by comma: ").split(",")

#to add data in th dictionary
user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs

print(user)

# to print the dictionary evry key in new line
for key, value in user.items():
    print(f"{key} : {value}")






