def bukaModeDictPandas():
    df = pandas.read_csv('praktikum.csv')
    dt = pandas.DataFrame.from_dict(df)
    print(dt)