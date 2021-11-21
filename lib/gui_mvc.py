# Interaction with eel gui
import eel
import os
import tkinter
import tkinter.filedialog as filedialog
import shutil

from .plot_graphs import plot
from . import set_max_ticks
from .speed_test_tracking import SpeedTestTracking

tracker = None
submitting = False


@eel.expose
def activate_submit():
    global submitting
    submitting = True
    return


@eel.expose
def select_folder():
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    directory_path = filedialog.askdirectory()
    return directory_path


@eel.expose
def create_tracking(interval, plots_path, max_ticks=None, expected_connection=None):
    if max_ticks:
        set_max_ticks(max_ticks)
    global tracker
    tracker = SpeedTestTracking(interval, plots_path, expected_connection, callback_function=runtime_plot)


@eel.expose
def start_tracking():
    if isinstance(tracker, SpeedTestTracking):
        tracker.start()


def on_close(route, url):
    if isinstance(tracker, SpeedTestTracking):
        if tracker.is_alive():
            tracker.prepared_stop()
            tracker.join()
            if os.path.isdir(os.environ['MODULE_PATH'] + '/gui/runtime'):
                shutil.rmtree(os.environ['MODULE_PATH'] + '/gui/runtime')
        else:
            return
    else:
        global submitting
        if submitting:
            submitting = False
            return
    exit(0)


def runtime_plot():
    path = os.environ['MODULE_PATH'] + '/gui/runtime'
    if os.path.isdir(path):
        shutil.rmtree(path)
    os.makedirs(path)
    plot(path)
    eel.update_html_plots()
