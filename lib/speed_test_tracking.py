# Manages the SpeedTest loop
import eel
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
        self.callback = kwargs['callback_function']
        self.gui = False
        if self.callback:
            self.gui = True
        threading.Thread.__init__(self)

    def run(self) -> None:
        lib.data_saver.create_data_file()
        st = speedtest.Speedtest()
        st.get_servers()
        counter = 1
        while self.cont:
            last_time = time.time()
            self.print_cmd('Fetching best server...')
            st.get_best_server()
            best = st.get_best_server()
            self.print_cmd(f'Using server located in {best["name"]}, {best["country"]}.')
            self.print_cmd('Testing download speed...')
            st.download()
            self.print_cmd('Testing upload speed...')
            st.upload()
            self.print_cmd('Saving test data...')
            res = st.results.dict()
            lib.data_saver.save_data(res['ping'], res['download'] / (1024**2), res['upload'] / (1024**2))
            self.print_cmd(f'\nTest {counter} completed')
            if self.gui:
                self.callback()
            current_time = time.time()
            next_time = last_time + self.interval_seconds
            while current_time - last_time < self.interval_seconds and self.cont:
                self.cls()
                if next_time - current_time >= 30:
                    self.print_cmd(f'Next test will start in {math.ceil((next_time - current_time) / 60)} minutes.')
                    if self.gui:
                        self.print_cmd('Close tracker to stop...')
                    else:
                        self.print_cmd('Press enter to stop...')
                else:
                    self.print_cmd(f'Next test will start in {round(next_time - current_time)} seconds.')
                    if self.gui:
                        self.print_cmd('Close tracker to stop...')
                    else:
                        self.print_cmd('Press enter to stop...')
                time.sleep(1)
                current_time = time.time()
            self.cls()
            counter += 1
        lib.plot_graphs.plot(self.path)
        lib.data_saver.clear_data_file()

    def prepared_stop(self):
        self.cont = False

    def cls(self):
        if self.gui:
            eel.clean_console()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')

    def print_cmd(self, msg):
        if self.gui:
            eel.write_console(msg)
        else:
            print(msg)
