import csv

with open('Mencobabikinfilecsv.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'Dio', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Despacito', 'dept': 'IT', 'birth_month': 'March'})