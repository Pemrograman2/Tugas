npm = input("Masukan NPM Anda: ")

for i in npm:
    a = int(i)

    if a != 0:
        if a % 2 == 0:
            print(i, end="")