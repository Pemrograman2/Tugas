def bukaModeDictCsv():
    with open('praktikum.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['Npm'], row['Nama'], row['Jurusan'])