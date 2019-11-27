import pandas

#No.3
def bukaModeListPandas():
    df = pandas.read_csv('tgs.csv')
    print(df)

#No.4
def PandasDictMode():
    df = pandas.read_csv('tgs.csv')
    dt = pandas.DataFrame.from_dict(df)
    print(dt)

#No.5
def ubahFormatTanggal():
    df = pandas.read_csv('tgs.csv', parse_dates=['tanggal lahir'])
    print(df)

#No.6
def ClmIdxChng():
    df = pandas.read_csv('tugas.csv')
    df.index = ['Row_1', 'Row_2']
    print(df)

#No.7
def ubahNamaKolom():
    df = pandas.read_csv('tugas.csv')
    df.columns =['Col_1', 'Col_2', 'Col_3', 'Col_4'] 
    print(df)

def PandasCSVWrite():
    df = pandas.read_csv('tgs.csv', 
            index_col='NPM', 
            parse_dates=['Tanggal Lahir'],
            header=0, 
            names=['NPM', 'Nama', 'Kelas', 'Tanggal Lahir'])
    df.to_csv('tgs5.csv')