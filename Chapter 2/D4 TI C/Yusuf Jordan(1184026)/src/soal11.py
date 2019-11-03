npm = input("Masukan NPM Anda: ")

for i in npm:

    number = int(i)

    if number > 1:

        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)