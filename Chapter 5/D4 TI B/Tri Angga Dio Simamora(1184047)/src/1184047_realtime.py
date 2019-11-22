import serial
import csv

def getData():
    serialArduino = serial.Serial("/dev/ttyACM0", 115200)
    serialArduino.flushInput()

    print(serialArduino)

def realtime():
    serialArduino = serial.Serial("/dev/ttyACM0", 9600)
    serialArduino.flushInput()

    with open('hasil_data.csv', 'w') as fileganteng:
        write = csv.writer(fileganteng)

        write.writerow(['data'])
        write.writerow([serialArduino])