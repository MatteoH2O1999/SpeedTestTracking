# Main launcher
import os
import sys
from sys import exit

from lib.speed_test_tracking import SpeedTestTracking
from lib import set_max_ticks


def main(interval, plots_path, max_ticks=None, expected_connection=None, callback=None):
    os.environ['MODULE_PATH'] = os.path.dirname(os.path.realpath(__file__))
    if max_ticks:
        set_max_ticks(max_ticks)
    tracker = SpeedTestTracking(interval, plots_path, expected_connection, callback_function=callback)
    tracker.start()
    input()
    tracker.prepared_stop()
    tracker.join()


if __name__ == '__main__':
    try:
        test_interval = int(sys.argv[1])
    except IndexError:
        test_interval = int(input('Enter interval between tests in seconds: '))
    try:
        path = sys.argv[2]
    except IndexError:
        path = input('Enter existing path for the plots: ')
    try:
        m_ticks = int(sys.argv[3])
    except IndexError:
        m_ticks = None
    try:
        expected_conn = sys.argv[4]
    except IndexError:
        expected_conn = None
    main(int(sys.argv[1]), sys.argv[2], m_ticks, expected_conn)
    exit(0)
