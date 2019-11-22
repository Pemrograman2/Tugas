import serial

def loopData():
    serialArduino = serial.Serial("/dev/ttyACM0", 115200)
    serialArduino.flushInput()
    while True:
        if serialArduino.isOpen():
            print("connection is open")