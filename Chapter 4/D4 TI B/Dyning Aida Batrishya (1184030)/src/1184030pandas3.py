import pandas

def SettformatTanggal():
    df = pandas.read_csv('1184030.csv', parse_dates=['tanggal lahir'])
    print(df)