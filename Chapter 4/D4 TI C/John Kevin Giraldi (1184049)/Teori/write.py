#Menulis File CSV dengan Fungsi writer dengan Library CSV
import csv

with open('CSV2.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, del=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['NPM';'NAMA';'JURUSAN'])
    csv_writer.writerow(['12346';'TONO';'CIPANAS'])
    csv_writer.writerow(['12355';'TEJO';'CICAHEUM'])
    csv_writer.writerow(['12367';'PAIJO';'JAKARTAMERAK'])
    csv_writer.writerow(['12378';'TUKIEM';'PULOGADUNG'])
    csv_writer.writerow(['12398';'ASEP';'TANAHABANG'])