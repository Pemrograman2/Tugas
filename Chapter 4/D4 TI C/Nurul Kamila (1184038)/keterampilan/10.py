def bacaCsvPandas () :
     try :
         df = pandas.read_csv ('praktikum.csv')
         print (dt)
         except SyntaxError :
             print ("Kesalahan penulisan ( syntax )")
         except NameError :
             print ("Variable tidak ada")
        except TypeError :
            print ("Tipe data salah")
        except :
            print ("Terjadi sebuah kesalahan")