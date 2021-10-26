# Manages the SpeedTest loop
import math
import os
import threading
import time

import speedtest

import lib.data_saver
import lib.plot_graphs


class SpeedTestTracking(threading.Thread):

    def __init__(self, interval, path, expected_connection=None, *args, **kwargs):
        self.interval_seconds = interval
        self.expected_connection = expected_connection
        self.cont = True
        self.path = path
        threading.Thread.__init__(self, *args, **kwargs)

    def run(self) -> None:
        lib.data_saver.create_data_file()
        st = speedtest.Speedtest()
        st.get_servers()
        counter = 1
        while self.cont:
            last_time = time.time()
            print('Fetching best server...')
            st.get_best_server()
            best = st.get_best_server()
            print(f'Using server located in {best["name"]}, {best["country"]}')
            print('Testing download speed...')
            st.download()
            print('Testing upload speed...')
            st.upload()
            print('Saving test data...')
            res = st.results.dict()
            lib.data_saver.save_data(res['ping'], res['download'] / (1024**2), res['upload'] / (1024**2))
            print(f'\nTest {counter} completed')
            time.sleep(2)
            current_time = time.time()
            next_time = last_time + self.interval_seconds
            while current_time - last_time < self.interval_seconds and self.cont:
                cls()
                if next_time - current_time >= 30:
                    print(f'Next test will start in {math.ceil((next_time - current_time) / 60)} minutes.\n'
                          f'Press enter to stop...')
                else:
                    print(f'Next test will start in {round(next_time - current_time)} seconds.\n'
                          f'Press enter to stop...')
                time.sleep(1)
                current_time = time.time()
            cls()
            counter += 1
        lib.plot_graphs.plot(self.path)
        lib.data_saver.clear_data_file()

    def prepared_stop(self):
        self.cont = False


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
