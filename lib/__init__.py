# Init module variables
import os

os.environ['MAX_PLOT_TICKS'] = str(6)


def set_max_ticks(n):
    os.environ['MAX_PLOT_TICKS'] = str(n)


def get_max_ticks():
    return int(os.environ['MAX_PLOT_TICKS'])
