import pandas
df = pandas.read_csv('source2.csv', 
            index_col='Pegawai', 
            parse_dates=['Diterima'], 
            header=0, 
            names=['Pegawai', 'Diterima','Gaji', 'Atit'])
print(df)