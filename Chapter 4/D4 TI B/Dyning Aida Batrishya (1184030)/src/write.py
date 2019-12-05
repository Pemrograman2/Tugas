import csv

with open('1184030.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
    csv.writer.writerow(['npm','namalengkap','kelas'])
    csv_writer.writerow(['1185065','Etika Khusnul Laeli','D4 TI 2B'])