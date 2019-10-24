# membuat variabel global
a = "Tari"

def help():
    # ini variabel lokal
    nama = "Lisa"
    # mengakses variabel lokal
    print (nama)
    print (a)
# mengakses variabel global
print (a)
# memanggil fungsi help()
help()


