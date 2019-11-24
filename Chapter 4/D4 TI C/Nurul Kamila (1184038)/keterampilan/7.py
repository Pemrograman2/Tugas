def ubahNamaKolom():
    df = pandas.read_csv('praktikum.csv')
    df.colums =['Col_1', 'Col_2', 'Col_3', 'Col_4']
    print(df)