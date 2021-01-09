import serial
import time
import sys

sleeptime = 1.5

ser = serial.Serial('/dev/ttyACM0', 115200)

ser.write('test'.encode())

def printAll():
    while ser.in_waiting:
        print(ser.readline().decode())


command = str(sys.argv[1]).encode()
print(command)

time.sleep(sleeptime)

printAll()

ser.write(command)

while not ser.in_waiting:  # Or: while self.ser.inWaiting():
    pass

time.sleep(sleeptime)

printAll()
