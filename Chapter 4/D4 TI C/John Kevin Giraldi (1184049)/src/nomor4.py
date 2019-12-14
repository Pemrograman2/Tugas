import pandas
def BukaModeDictPandas():
df = pandas.read_csv('CSV1.csv')
dt = pandas.DataFrame.from_dict(df)
print(dt)