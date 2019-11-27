import pandas

#No.3
def bukaModeListPandas():
    df = pandas.readCSV('tgs.csv')
    print(df)

#No.4
def PandasDictMode():
    df = pandas.rreadCSV('tgs.csv')
    dt = pandas.DataFrame.from_dict(df)
    print(dt)

#No.5
def ubahFormatTanggal():
    df = pandas.readCSV('tgs.csv', parse_dates=['tanggal lahir'])
    print(df)

#No.6
def ClmIdxChng():
    df = pandas.readCSV('tugas.csv')
    df.index = ['Row_1', 'Row_2']
    print(df)

#No.7
def ubahNamaKolom():
    df = pandas.readCSV('tugas.csv')
    df.columns =['Col_1', 'Col_2', 'Col_3', 'Col_4'] 
    print(df)

def PandasCSVWrite():
    df = pandas.readCSV('tgs.csv', 
            index_col='NPM', 
            parse_dates=['Tanggal Lahir'],
            header=0, 
            names=['NPM', 'Nama', 'Kelas', 'Tanggal Lahir'])
    df.to_csv('tgs5.csv')