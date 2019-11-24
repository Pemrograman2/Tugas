#Fungsi Try Except 
def bacaCsvPandas():
    try:
        df = pandas.read_csv('Praktikum 1.csv')
        print(dt)
    except SyntaxError:
        print("Kesalahan penulisan (syntax)")
    except NameError:
        print("Variable belum ada")
    except TypeError:
        print("Tipe data belum benar")
    except:
        print("Terjadi sebuah kesalahan")

bacaCsvPandas()