npm = input("Masukkan NPM anda: ")

# nomor 1
print("Soal nomor 1")
nPm = int(npm)
print(nPm % 3)

print("###  ###  #########  ###   ###  #########  ###   ###    ###########")
print("###  ###  #########  ###   ###  #########  ###   ###    ##########")
print("###  ###  ###   ###  ###   ###  ###   ###  ###   ###          ###")
print("###  ###  ###   ###  ###   ###  ###   ###  ###   ###         ###")
print("###  ###  #########  #########  ###   ###  #########        ###")
print("###  ###  ###   ###        ###  ###   ###        ###       ###")
print("###  ###  ###   ###        ###  ###   ###        ###      ###")
print("###  ###  #########        ###  #########        ###     ###")
print("###  ###  #########        ###  #########        ###    ###")

# nomor 2
print("soal nomor 2")

nPm = int(npm[-2:])

for i in range(nPm):
    print("Halo, " + npm + " apa kabar?")

# nomor 3
print("soal nomor 3")

nPm = npm[-3:]

b = 0

for i in nPm:
    c = int(i) + b
    b = c

for i in range(b):
    print("Halo, " + nPm + " apa kabar?")

# nomor 4
print("soal nomor 4")

nPm = npm[-3]

for i in nPm:
    print("Halo, " + nPm + " apa kabar?")

# nomor 5
print("soal nomor 5")

string = "abcdefg"

index = 0

for i in string:
    print(i + " = " + npm[index])
    index += 1

# nomor 6
print("soal nomor 6")

a = 0
b = 0
for i in npm:
    c = int(i) + b
    b = c
    a += 1

print(b)

# nomor 7
print("soal nomor 7")

a = 0
b = 0
for i in npm:
    c = int(i) * b
    b = c
    a += 1

print(b)

# nomor 8
print("soal nomor 8")

for i in npm:
    print(i)

# nomor 9
print("soal nomor 9")

for i in npm:
    a = int(i)

    if a != 0:
        if a % 2 == 0:
            print(i, end="")

# nomor 10
print("soal nomor 10")

for i in npm:
    a = int(i)

    if a != 0:
        if a % 2 == 1:
            print(i, end="")

# nomor 11
print("soal nomor 11")
for i in npm:

    number = int(i)

    if number > 1:

        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)
