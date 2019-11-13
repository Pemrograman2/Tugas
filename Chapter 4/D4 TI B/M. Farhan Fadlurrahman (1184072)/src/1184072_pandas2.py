import pandas
df = pandas.read_csv('source2.csv')
dt = pandas.DataFrame.from_dict(df)
print(dt)