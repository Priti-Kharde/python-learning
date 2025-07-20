# names = ['priit','kalyani','reshma']
# print(max(names, key = lambda i : len(i)))

# students = [
#     {'name': "priti",'score':90},
#     {'name': "kalyani",'score':70},
#     {'name': 'reshma', 'score': 46}
# ]
# print(max(students, key=lambda student: len(student['name'])))

# print(min(students, key = lambda item: item.get('score')))

# print(max(students, key = lambda item: item.get('score'))['name'])



stud = {
    'harshit' : {'score': 50, 'age': 24},
    'mohit' : {'score': 75, 'age': 19},
    'rohit' : {'score': 86, 'age': 45},
}
# print(max(stud, key = lambda item :stud[item]['score']))

nameee = max(stud, key = lambda name: stud['name']['score'])
print(nameee)