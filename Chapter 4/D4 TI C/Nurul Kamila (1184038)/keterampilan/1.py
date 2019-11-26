def bukaModeListCsv():
    with open('praktikum.csv') as csv_file:
        csv_reader = csv.reader(csv_file , delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])