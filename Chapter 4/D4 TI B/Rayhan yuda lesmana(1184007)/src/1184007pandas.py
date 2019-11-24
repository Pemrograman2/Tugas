import pandas

#3
def bukaModeListPandas():
    df = pandas.read_csv('tugas.csv')
    print(df)

#4
def bukaModeDictPandas():
    df = pandas.read_csv('tugas.csv')
    dt = pandas.DataFrame.from_dict(df)
    print(dt)
    
#5
def ubahFormatTanggal():
    df = pandas.read_csv('tugas.csv', parse_dates=['tanggal lahir'])
    print(df)

#6
def ubahIndexKolom():
    df = pandas.read_csv('tugas.csv')
    df.index = ['Row_1', 'Row_2']
    print(df)

#7
def ubahNamaKolom():
    df = pandas.read_csv('tugas.csv')
    df.columns =['Col_1', 'Col_2', 'Col_3', 'Col_4'] 
    print(df)
    
def tulisCsvPandas():
    df = pandas.read_csv('tugas.csv', 
            index_col='NPM', 
            parse_dates=['Tanggal Lahir'],
            header=0, 
            names=['NPM', 'Nama', 'Kelas', 'Tanggal Lahir'])
    df.to_csv('tugas5.csv')
    