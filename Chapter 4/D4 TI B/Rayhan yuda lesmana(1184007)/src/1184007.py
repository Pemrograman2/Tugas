import csv

with open('tugas.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[0], row[1], row[2])
        
import csv

with open('tugas.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['npm'], row['nama'], row['kelas'])
        
import csv

with open('tugas1.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['npm', 'nama', 'kelas'])
    csv_writer.writerow(['1184002', 'Udin', 'D4TI2B'])
    csv_writer.writerow(['1184008', 'Asep', 'D4TI2B'])

import csv

with open('tugas2.csv', mode='w') as csv_file:
    fieldnames = ['npm', 'nama', 'kelas']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'npm': '1184098', 'nama': 'Budi', 'kelas': 'D4TI2B'})
    writer.writerow({'npm': '1184096', 'nama': 'Agus', 'kelas': 'D4TI2B'})
    
import pandas

df = pandas.read_csv('tugas.csv')
print(df)

import pandas

df = pandas.read_csv('tugas.csv')
df.to_csv('tugas3.csv')
    
def bacaCsvPandas():
    try:
        df = pandas.read_csv('tugas.csv')
        print(dt)
    except SyntaxError:
        print("Kesalahan penulisan (syntax)")
    except NameError:
        print("Variable tidak ada")
    except TypeError:
        print("Tipe data salah")
    except:
        print("Terjadi sebuah kesalahan")

bacaCsvPandas()