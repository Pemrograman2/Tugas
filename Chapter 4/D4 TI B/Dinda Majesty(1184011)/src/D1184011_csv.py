import csv

def CsvList():
    with open('FCSV.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Nama Kolom adalah {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t Nomor : {row[0]}, Nama Klub : {row[1]}, Jumlah Main : {row[2]}, Poin : {row[3]}.')
                line_count += 1
                print(f'Jumlah Total {line_count} lines.')

def CsvDict():
    with open('dictionary.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Nama Kolom adalah {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t First Name : {row["first_name"]} Last Name : {row["last_name"]}.')
                line_count += 1
                print(f'Jumlah Total {line_count} lines.')
