import pandas
df = pandas.read_csv('source2.csv', 
            index_col='Pegawai', 
            parse_dates=['Diterima'], 
            header=0, 
            names=['Pegawai', 'Diterima','Gaji', 'Atit'])
df.to_csv('data_yang_barusan_di_ubah_ea.csv')