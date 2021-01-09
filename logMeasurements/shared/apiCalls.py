from time import sleep
from shared.util.util import timestamp_print
import requests
from subprocess import check_output

post_to_server = True


def wait_for_wifi():
    while True:
        wifi_ip = check_output(['hostname', '-I'])
        if wifi_ip is not None:
            return
        timestamp_print("No internet")
        sleep(10)


class ApiCalls:
    host = 'https://hansenbrew.dk/'

    def __init__(self, url):
        self.url = url

    def post_log_to_server(self, data):
        if post_to_server:
            while True:
                wait_for_wifi()
                try:
                    x = requests.post(self.host + self.url, timeout=3, data=data)
                    print(str(x.status_code))
                    x.raise_for_status()
                    return True
                    
                except requests.exceptions.Timeout:
                    timestamp_print("Post to server - timeout")
                except requests.exceptions.HTTPError:
                    timestamp_print("Bad status code: " + str(x.status_code))
                    return False
                except requests.exceptions.RequestException as e:
                    timestamp_print("Post to server - ConnectionError" + e)
                except Exception as e:
                    timestamp_print("Some exception from API-calls: " + e)
