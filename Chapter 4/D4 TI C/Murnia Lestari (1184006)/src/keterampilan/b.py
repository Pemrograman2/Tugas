import csv 
def bukaModeDictCsv():
    with open('praktikum 1.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['NPM'], row['NAMA'], row['MATAKULIAH'])

def tulisCsv():
    with open('praktikum5.csv', mode='w') as csv_file:
        fieldnames = ['NPM', 'NAMA', 'MATAKULIAH', 'RUANG']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'NPM': '1184005', 'nama': 'Ter Stegen', 'kelas': 'D4TI2B', 'tanggal lahir': '30/03/2000'})
        writer.writerow({'': '1184006', 'nama': 'Coutinho', 'kelas': 'D4TI2B', 'tanggal lahir': '30/04/2000'})
