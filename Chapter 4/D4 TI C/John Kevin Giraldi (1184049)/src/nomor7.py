import pandas
def ubahNamaKolom():
    df = pandas.read_csv('CSV1.csv')
    df.columns =['Col_1', 'Col_2', 'Col_3', 'Col_4']
    print(df)
