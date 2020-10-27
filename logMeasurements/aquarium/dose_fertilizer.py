from datetime import datetime, timedelta
from threading import Timer
from shared import megaApi
from shared.apiCalls import ApiCalls
from shared.util.util import timestamp_print


def post_fertilizer_log(successful_dosing):
    successful_dosing: bool = successful_dosing in ["true", "1", True, 1]
    data = {"successfulDosing": successful_dosing}
    timestamp_print("fertilizer data: " + str(data))
    ApiCalls('aquarium/postfertilizerlog/').post_log_to_server(data)


class TimeChecker:
    mega: megaApi.MegaApi
    time = datetime.today()
    # 5 min delay
    timer_max_delay = 60*5
    
    def __init__(self, time):
        self.time = time
        self.fertilize_time_controller()

    @classmethod
    def dosing_version(cls, time, mega):
        cls.time = time
        cls.mega = mega

    def fertilize_time_controller(self):
        now = datetime.today()
        next_time = now.replace(
            day=now.day,
            hour=self.time.hour,
            minute=self.time.minute,
            second=self.time.second,
            microsecond=0
        )
        secs = (next_time - now).total_seconds()
        if secs <= self.timer_max_delay:
            if secs < 0:
                secs += timedelta(days=1).total_seconds()
            else:
                t = Timer(self.timer_max_delay, self.fertilize)
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
            self.mega.relay_timed(0, 5)
        t = Timer(self.timer_max_delay, self.fertilize_time_controller)
        t.start()
