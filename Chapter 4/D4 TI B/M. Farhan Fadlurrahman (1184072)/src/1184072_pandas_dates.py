import pandas
df = pandas.read_csv('source2.csv', parse_dates=['Hire Date'])
print(df)