import csv

#1
def bukaModeListCsv():
    with open('tugas.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])

#2            
def bukaModeDictCsv():
    with open('tugas.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['nama'], row['kelas'])

def tulisCsv():
    with open('tugas6.csv', mode='w') as csv_file:
        fieldnames = ['npm', 'nama', 'kelas', 'tanggal lahir']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'npm': '1184098', 'nama': 'Udin', 'kelas': 'D4TI2B', 'tanggal lahir': '29/06/1972'})
        writer.writerow({'npm': '1184078', 'nama': 'Jony', 'kelas': 'D4TI2B', 'tanggal lahir': '13/02/1987'})
