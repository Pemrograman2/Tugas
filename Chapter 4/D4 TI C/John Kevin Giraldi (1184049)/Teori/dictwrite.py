#Membaca File CSV dengan Fungsi DictWriter dengan Library CSV
import csv

with open('CSV3.csv', mode='w') as csv_file:
    fieldnames = ['NPM', 'NAMA', 'JURUSAN']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'NPM': '12346', 'NAMA': 'TONO', 'JURUSAN': 'CIPANAS'})
    writer.writerow({'NPM': '12355', 'NAMA': 'TEJO', 'JURUSAN': 'CICAHEUM'})
    writer.writerow({'NPM': '12367', 'NAMA': 'PAIJO', 'JURUSAN': 'JAKARTAMERAK'})
    writer.writerow({'NPM': '12378', 'NAMA': 'TUKIEM', 'JURUSAN': 'PULOGADUNG'})
    writer.writerow({'NPM': '12398', 'NAMA': 'ASEP', 'JURUSAN': 'TANAHABANG'})
    