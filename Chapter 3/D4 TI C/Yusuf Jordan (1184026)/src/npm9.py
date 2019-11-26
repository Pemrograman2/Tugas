def npm9(npm):
    npm = input("Masukan NPM anda: ")
    
    for i in npm:
        a = int(i)
        if a != 0:
            if a % 2 == 1:
                print(i, end="")
