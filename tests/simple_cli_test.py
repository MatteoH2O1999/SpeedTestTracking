# Tests speedtest for a single cycle
import os
import shutil
import time
import pytest

from lib.speed_test_tracking import SpeedTestTracking


def is_not_timeout(err, *args):
    return not issubclass(err[0], TimeoutError)


@pytest.mark.timeout(180)
@pytest.mark.flaky(max_runs=3, min_passes=1, rerun_filter=is_not_timeout)
def test_one_cycle():
    os.environ['MODULE_PATH'] = os.path.dirname(os.path.realpath(__file__))
    tracker = SpeedTestTracking(600, './plots', expected_connection=None, callback_function=None)
    tracker.start()
    time.sleep(10)
    tracker.prepared_stop()
    tracker.join()
    assert os.path.isfile('./plots/download.png')
    assert os.path.isfile('./plots/upload.png')
    assert os.path.isfile('./plots/ping.png')
    assert os.path.isfile('./plots/data.xlsx')
    shutil.rmtree('./plots')
