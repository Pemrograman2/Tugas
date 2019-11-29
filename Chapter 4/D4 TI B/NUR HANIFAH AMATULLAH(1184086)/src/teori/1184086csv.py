import csv

#no1
def listCsv():
    with open('Book1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])

#no2
def dictCsv():
    with open('Book1.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['NPM'], row['Nama'], row['Jurusan'])



def tulisCsv():
    with open('Book2.csv', mode='w') as csv_file:
        fieldnames = ['NPM','Nama','Jurusan']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'NPM': '1184020', 'Nama': 'Dudu', 'Jurusan':'TI'})
        writer.writerow({'NPM': '1184030', 'Nama': 'Didi', 'Jurusan':'LB'})
