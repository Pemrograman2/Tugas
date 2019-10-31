def NPM2():
    npm = input("NPM: ")
    val = int(npm[5:7])
    total = 0
    
    print("Input: "+npm)
    print("Output: ")
    
    while val > 0:
        print("Halo, "+npm+" Apa Kabar ?")
        val = val - 1
        total = total + 1
        
    print(".........."+str(total)+"Kali..........")