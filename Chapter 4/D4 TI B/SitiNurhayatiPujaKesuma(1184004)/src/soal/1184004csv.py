import csv

#no1
def listCsv():
    with open('contoh1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])

#no2
def dictCsv():
    with open('contoh1.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['nama'], row['kelas'])



def tulisCsv():
    with open('contoh1.csv', mode='w') as csv_file:
        fieldnames = ['no', 'nama', 'npm']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'no': '3', 'nama': 'Pute', 'NPM':'1184004'})
        writer.writerow({'no': '8', 'nama': 'Bintang', 'NPM':'1184020'})