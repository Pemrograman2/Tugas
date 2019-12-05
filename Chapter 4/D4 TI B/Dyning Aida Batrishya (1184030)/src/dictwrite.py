import csv

with open('1184030.csv',mode='w') as csv_file:
    fieldnames = ['npm','namalengkap','kelas']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'npm': '11840300','namalengkap': 'Dyning Aida Batrishya','kelas' :'D4 TI 2B'})