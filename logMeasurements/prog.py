from aquarium.dose_fertilizer import TimeChecker
from shared.util.util import timestamp_print
from shared.apiCalls import ApiCalls
from threading import Timer
from datetime import datetime, timedelta, time
import time as delay

debug = False

if not debug:
    from shared.megaApi import MegaApi


class Program:
    dose_time = time(hour=13, minute=5, second=0)

    if not debug:
        mega = MegaApi()
        time_checker = TimeChecker(dose_time, mega)
        time_checker.fertilize_time_controller()
    else:
        time_checker = TimeChecker(dose_time)

    def __init__(self):
        timestamp_print("Init")
        self.measure()

    def measure(self):
        data = {"temp": 0, "ph": 0, "TDS": 0}

        posted = False
        while not posted:
            if not debug:
                data = {"temp": self.mega.get_water_temp(), "ph": self.mega.get_ph(), "TDS": self.mega.get_tds()}
                timestamp_print(str(data))
            posted = ApiCalls('aquarium/postautolog/').post_log_to_server(data)
        self.measure_timer()

    def measure_timer(self):
        now = datetime.today()
        next_measure_time = now + timedelta(minutes=10 - (now.minute % 10)) - timedelta(seconds=now.second)

        secs = (next_measure_time - now).total_seconds()
        timestamp_print("Next measure in:  " + str(int(secs / 60)) + "min and " + str(secs % 60) + "secs")

        t = Timer(secs, self.measure)
        t.start()


Program()

while True:
    delay.sleep(60 * 60 * 24)
