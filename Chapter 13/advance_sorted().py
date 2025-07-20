# fruits = ('grapes','apple','banana')
# print(sorted(fruits))

students = [
    {'name': 'priti', 'score': 95920},
    {'name': 'kalyani', 'score': 74233320},
    {'name': 'amar', 'score': 55}
]
# print(sorted(students, key = lambda d : d['score']))

print(sorted(students, key = lambda d : d['score'], reverse=True))