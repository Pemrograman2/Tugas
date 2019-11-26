import pandas
def ubahIndexKolom():
    df = pandas.read_csv('praktikum.csv')
    df.index = ['Row_1', 'Row_2']
    print(df)
