
#Penggunaan Fungsi-Fungsi Format CSV

#Membaca file CSV dengan fungsi Reader dengan menggunaka library CSV
import csv 

with open('teori1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)

##Membaca File CSV dengan Fungsi DictReader dengan library CSV
import csv

with open('teori2.csv',mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['npm'], row['nama'], row['kelas'])

        
#Menulis File CSV dengan Fungsi writer dengan library CSV    
import csv

with open('teori3.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['npm', 'nama', 'kelas'])
    csv_writer.writerow(['1184036', 'Muchamad Innal Kariem','2B'])
    csv_writer.writerow(['1184222','Apliriano Kusnandar','2J'])
    

#Menulis File CSV dengan Fungsi DictWriter dengan library CSV
import csv

with open('teori4.csv', mode='w') as csv_file:
    fieldnames = ['npm', 'nama', 'kelas']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'npm': '1184036', 'nama': 'innal', 'kelas':'2B'})
    writer.writerow({'npm': '1184037', 'nama': 'Lanni', 'kelas':'2B'})
    writer.writerow({'npm': '1184038', 'nama': 'Annil', 'kelas':'2B'})
