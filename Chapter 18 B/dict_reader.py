# from csv import DictReader
# # ordered dict
# with open('file.csv','r') as f:
#     csv_reader = DictReader(f)
#     for row in csv_reader:
#         print(row)
#         print(row['name']) # prints names in csv file



from csv import DictReader
# ordered dict
with open('file.csv','r') as f:
    csv_reader = DictReader(f,delimiter='|')
    for row in csv_reader:
        print(row['email'])