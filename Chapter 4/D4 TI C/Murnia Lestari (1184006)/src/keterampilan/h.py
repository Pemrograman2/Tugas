import pandas
def tulisCsvPandas():
    df = pandas.read_csv('Praktikum 1.csv', 
            index_col='NPM', 
            parse_dates=['Ruang'],
            header=0, 
            names=['NPM', 'NAMA', 'MATAKULIAH', 'RUANG'])
    df.to_csv('Praktikum 6.csv')
    