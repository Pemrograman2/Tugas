nilai_ips = 90
ekskul = 'true'
les = 'true'

if nilai_ips > 80
    print("Nilai ips anda diatas KKM")
    if ekskul:
        print("Anda aktif disekolah")
        
    else:
        print("Anda tidak aktif disekolah")
        
    if les:
         print("Anda aktif diles")
        
    else:
        print("Anda tidak aktif diles")
else:
    print("Nilai anda masih dibawah KKM")