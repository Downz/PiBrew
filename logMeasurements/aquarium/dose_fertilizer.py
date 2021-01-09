from datetime import datetime, timedelta, time
from threading import Timer
from shared import megaApi
from shared.apiCalls import ApiCalls
from shared.util.util import timestamp_print


def post_fertilizer_log(successful_dosing, dose_amount):
    successful_dosing: bool = successful_dosing in ["true", "1", True, 1]
    data = {"successfulDosing": successful_dosing, "doseAmount": dose_amount}
    timestamp_print("fertilizer data: " + str(data))
    ApiCalls('aquarium/postfertilizerlog/').post_log_to_server(data)


class TimeChecker:
    mega: megaApi.MegaApi
    time: time
    # 10 min delay
    timer_max_delay = 60*10
    dose_amount = 7
    
    def __init__(self, time, mega):
        self.time = time
        self.mega = mega


    def fertilize_time_controller(self):
        now = datetime.today()
        next_time = now.replace(
            year=now.year,
            day=now.day,
            hour=self.time.hour,
            minute=self.time.minute,
            second=self.time.second,
            microsecond=0
        )
        secs = (next_time - now).total_seconds()
        timestamp_print("Dosetime: " + str(self.time) + ", now: " + str(now) + ", next: " + str(next_time) + ", Secs to next fertilizerdose: " + str(secs)) 
        
        if 0 < secs <= self.timer_max_delay:
            t = Timer(secs + 10, self.fertilize)
            t.start()
            return

        self.wait_longer()

    def wait_longer(self):
        timestamp_print("wait longer - dose Fertilizer")
        t = Timer(self.timer_max_delay, self.fertilize_time_controller)
        t.start()

    def fertilize(self):
        timestamp_print("Fertilize")
        if self.mega:
            success = self.mega.relay_timed(0, self.dose_amount)
            post_fertilizer_log(success, self.dose_amount)

        t = Timer(self.timer_max_delay, self.fertilize_time_controller)
        t.start()
