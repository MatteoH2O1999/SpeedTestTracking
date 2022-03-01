import os
import time

from lib.speed_test_tracking import SpeedTestTracking


def main():
    os.environ['MODULE_PATH'] = os.path.dirname(os.path.realpath(__file__))
    tracker = SpeedTestTracking(600, './plots', None, callback_function=None)
    tracker.start()
    time.sleep(10)
    tracker.prepared_stop()
    tracker.join()


if __name__ == '__main__':
    main()
