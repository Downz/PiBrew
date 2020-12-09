import serial
from shared.util.util import timestamp_print

class MegaApi:

    def __init__(self):
        #self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=10)
        #self.ser = serial.Serial('/dev/serial0', 115200, timeout=10) 
        self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=10)

    def clear_serial_read(self):
        timestamp_print("Flush")
        self.ser.reset_input_buffer()

    def get_water_temp(self):
        self.clear_serial_read()
        command = 'wt'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_internal_temp(self):
        self.clear_serial_read()
        command = 'ait'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_internal_pressure(self):
        self.clear_serial_read()
        command = 'aip'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_external_temp(self):
        self.clear_serial_read()
        command = 'aet'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_external_pressure(self):
        self.clear_serial_read()
        command = 'aep'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_calibrate(self):
        self.clear_serial_read()
        command = 'c'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_sol_releases(self):
        self.clear_serial_read()
        command = 'sr'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def sol_open(self):
        self.clear_serial_read()
        command = 'so'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def sol_close(self):
        self.clear_serial_read()
        command = 'sc'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def sol_timed(self, time):
        self.clear_serial_read()
        command = 'sr' + str(time)
        command.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def sol_clear_releases(self):
        self.clear_serial_read()
        command = 'sl'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def set_pressure_delta(self, delta):
        self.clear_serial_read()
        command = 'ad' + str(delta)
        self.ser.write(command.encode())
        return self.ser.readline().decode()
    
    def relay_open(self, relay_number):
        self.clear_serial_read()
        command = 'ro' + str(relay_number)
        self.ser.write(command.encode())
        return self.ser.readline().decode()

    def relay_close(self, relay_number):
        self.clear_serial_read()
        command = 'rc' + str(relay_number)
        self.ser.write(command.encode())
        return self.ser.readline().decode()

    def relay_timed(self, relay_number, time):
        self.clear_serial_read()
        command = 'rt' + str(relay_number) + str(time)
        self.ser.write(command.encode())
        return self.ser.readline().decode()

    def get_ph(self):
        self.clear_serial_read()
        command = 'p'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_tds(self):
        self.clear_serial_read()
        command = 't'
        self.ser.write(command.encode())
        return self.ser.readline().decode()

