import serial
import threading
from shared.util.util import timestamp_print

class MegaApi:

    def __init__(self):
        #self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=10)
        #self.ser = serial.Serial('/dev/serial0', 115200, timeout=10) 
        self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=10)
        self.lock = threading.Lock()


    def __clear_serial_read(self):
        timestamp_print("Flush")
        self.ser.reset_input_buffer()

    
    def __send_mega_command(self, command):
        self.lock.acquire()
        try:
            self.__clear_serial_read()
            self.ser.write(command.encode())
            response = self.ser.readline().decode()
        finally:
            self.lock.release()
        return response
    

    def get_water_temp(self):
        return self.__send_mega_command("wt")

    def get_internal_temp(self):
        return self.__send_mega_command("ait")

    def get_internal_pressure(self):
        return self.__send_mega_command("aip")

    def get_external_temp(self):
        return self.__send_mega_command("aet")

    def get_external_pressure(self):
        return self.__send_mega_command("aep")

    def get_calibrate(self):
        return self.__send_mega_command("c")

    def get_sol_releases(self):
        return self.__send_mega_command("sr")

    def sol_open(self):
        return self.__send_mega_command("so")

    def sol_close(self):
        return self.__send_mega_command("sc")

    def sol_timed(self, time):
        return self.__send_mega_command("sr" + str(time))

    def sol_clear_releases(self):
        return self.__send_mega_command("sl")

    def set_pressure_delta(self, delta):
        return self.__send_mega_command("ad" + str(delta))
    
    def relay_open(self, relay_number):
        return self.__send_mega_command("ro" + str(relay_number))

    def relay_close(self, relay_number):
        return self.__send_mega_command("rc" + str(relay_number))

    def relay_timed(self, relay_number, time):
        return self.__send_mega_command("rt" + str(relay_number) + str(time))

    def get_ph(self):
        return self.__send_mega_command("p")

    def get_tds(self):
        return self.__send_mega_command("t")

