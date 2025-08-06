from csv import writer
with open('file2.csv','w', newline ='') as f:
    csv_writer = writer(f)

    # methods writerow, writerows
    # csv_writer.writerow(['name','country'])
    # csv_writer.writerow(['Priti','India'])
    # csv_writer.writerow(['Kalyani','INDIA'])

    csv_writer.writerows([['name','country'],['priti','India'],['kalyani','Australia']])
    

