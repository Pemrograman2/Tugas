var1 = input("Variable String: ")
var2 = input("Variable Integer: ")

string = str(var1)
integer = int(var2)
try:
    jml = string+integer
except Exception:
    print("String tidak bisa dijumlah dengan integer, string harus di casting menjadi integer dulu")