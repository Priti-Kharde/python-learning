from csv import DictWriter
with open('file3.csv','w',newline='') as f:
    csv_writer = DictWriter(f,fieldnames=['name','salary','age'])
    csv_writer.writeheader()

    # csv_writer.writerow(
    #     {
    #         'name' : 'priti',
    #         'salary' : 50000,
    #         'age' : 20
    #     }
    # )
    # csv_writer.writerow(
    #     {
    #         'name' : 'reshma',
    #         'salary' : 63000,
    #         'age' : 31
    #     }
    # )
    # csv_writer.writerow(
    #     {
    #         'name' : 'kalyani',
    #         'salary' : 21800,
    #         'age' : 18
    #     }
    # )

    csv_writer.writerows([
        {'name' : 'chaitanya','salary': 5234,'age' : 20},
        {'name' : 'kajal','salary': 75213,'age' : 52},
        {'name' : 'rutuja','salary': 100,'age' : 10}
    ])