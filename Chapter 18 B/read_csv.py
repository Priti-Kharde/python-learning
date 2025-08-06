from csv import reader

with open('file.csv','r') as f:
    csv_reader = reader(f)
    # print(csv_reader)
    # print(type(csv_reader))
    next(csv_reader)

    
    for row in csv_reader:
        print(row)


