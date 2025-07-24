def to_power(x): # X = power kay asel te
    def cal_power(n): # jya numbe cha power havay to number
        return n ** x
    return cal_power
cube = to_power(3)
print(cube(5))

square = to_power(8)
print(square(2))