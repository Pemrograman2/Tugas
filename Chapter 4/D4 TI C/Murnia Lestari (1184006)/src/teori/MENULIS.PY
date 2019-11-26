#Menulis File CSV dengan Fungsi writer dengan library CSV    
import csv

with open('praktikum 2.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['NPM';'NAMA';'MATAKULIAH'])
    csv_writer.writerow(['11840O6';'MURNIA LESTARI';'PEMROGRAMAN 2'])
    csv_writer.writerow(['1184038';'NURUL KAMILA' ;'PEMROGRAMAN 2'])
