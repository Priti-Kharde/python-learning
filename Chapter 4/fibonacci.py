def fibonacci(number):
    a = 0 #first no.of series
    b = 1 #second
    if number == 1:
        print(a)
    elif number == 2:
        print(a,b)
    else:
        print(a,b, end = " ")
        for i in range(number-2):
            c = a + b
            a = b
            b = c
            print(b, end = " ")
number = int(input("how many numbers you want in your fibonacci series: "))
fibonacci(number)