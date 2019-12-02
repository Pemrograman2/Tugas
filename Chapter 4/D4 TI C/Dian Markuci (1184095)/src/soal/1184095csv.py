import csv

#1
def listCsv():
    with open('contoh.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])

#2
def dictCsv():
    with open('contoh.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['nama'], row['kelas'])



def tulisCsv():
    with open('contoh2.csv', mode='w') as csv_file:
        fieldnames = ['npm', 'nama', 'jurusan']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'npm': '3', 'nama': 'Bang', 'jurusan':'TI'})
        writer.writerow({'npm': '4', 'nama': 'Dhedhe', 'jurusan':'TI'})
        
        