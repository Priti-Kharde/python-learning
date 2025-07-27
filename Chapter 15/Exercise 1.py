def even_generator(number):
    for num in range(1, number + 1):
        if num % 2 == 0:
            yield(num)
for num in even_generator(4):
    print(num)