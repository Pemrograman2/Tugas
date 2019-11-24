import pandas
def ubahFormatTanggal():
    df = pandas.read_csv('praktikum.csv', parse_dates=['tanggal lahir'])
    print(df)