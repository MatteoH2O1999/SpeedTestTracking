import eel
import os

from lib.gui_mvc import on_close


if __name__ == '__main__':
    os.environ['MODULE_PATH'] = os.path.dirname(os.path.realpath(__file__))
    eel.init('gui')
    eel.start('launcher.html', close_callback=on_close)
