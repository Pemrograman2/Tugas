class Tugas(object):

    def __init__(self, npm):
        self.npm = npm

    def nomor1(self):
        print("Soal nomor 1")
        nPm = int(self.npm)
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

    def nomor2(self):
        # nomor 2
        print("soal nomor 2")

        nPm = int(self.npm[-2:])

        for i in range(nPm):
            print("Halo, " + self.npm + " apa kabar?")

    def nomor3(self):
        # nomor 3
        print("soal nomor 3")

        nPm = self.npm[-3:]

        b = 0

        for i in nPm:
            c = int(i) + b
            b = c

        for i in range(b):
            print("Halo, " + nPm + " apa kabar?")

    def nomor4(self):
        # nomor 4
        print("soal nomor 4")

        nPm = self.npm[-3]

        for i in nPm:
            print("Halo, " + nPm + " apa kabar?")

    def nomor5(self):
        # nomor 5
        print("soal nomor 5")

        string = "abcdefg"

        index = 0

        for i in string:
            print(i + " = " + self.npm[index])
            index += 1

    def nomor6(self):
        # nomor 6
        print("soal nomor 6")

        a = 0
        b = 0
        for i in self.npm:
            c = int(i) + b
            b = c
            a += 1

        print(b)

    def nomor7(self):
        # nomor 7
        print("soal nomor 7")

        a = 0
        b = 0
        for i in self.npm:
            c = int(i) * b
            b = c
            a += 1

        print(b)

    def nomor8(self):
        # nomor 8
        print("soal nomor 8")

        for i in self.npm:
            print(i)

    def nomor9(self):
        # nomor 9
        print("soal nomor 9")

        for i in self.npm:
            a = int(i)

            if a != 0:
                if a % 2 == 0:
                    print(i, end="")

    def nomor10(self):
        # nomor 10
        print("soal nomor 10")

        for i in self.npm:
            a = int(i)

            if a != 0:
                if a % 2 == 1:
                    print(i, end="")

    def nomor11(self):
        # nomor 11
        print("soal nomor 11")
        for i in self.npm:

            number = int(i)

            if number > 1:

                for i in range(2, number):
                    if (number % i) == 0:
                        break
                else:
                    print(number)
