#kondisi didalam kondisi
a = -25
if a < 0 :
    print (a, "adalah bilangan negatif")
    if a < 0 :
        print (a, "adalah bilangan negatif yang lebih kecil dari -5")
    else:
        print (a, "adalah bilangan kurang dari 100")
elif a > 0:
    print ( a,"adalah bilangan positif")
else:
    print (a, "adalah bilangan prima")
    
    
