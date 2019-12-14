import pandas
def ubahFormatTanggal():
    df = pandas.read_csv('CSV1.csv', parse_dates=['tanggal lahir'])
    print(df)