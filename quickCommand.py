import serial
import time
import sys
 
ser = serial.Serial('/dev/ttyACM0', 115200)
command = str(sys.argv[1]).encode()
print(command)

ser.write(command)
while not ser.in_waiting:  # Or: while self.ser.inWaiting():
    pass
print(ser.readline().decode())
