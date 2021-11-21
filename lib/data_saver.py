# Saves data to csv
import os
import time


def create_data_file():
    path = os.environ['MODULE_PATH'] + '/runtime'
    try:
        os.makedirs(path, exist_ok=True)
    except OSError:
        raise RuntimeError
    with open(path + '/data.csv', 'w') as data_file:
        data_file.write('time;ping;download;upload\n')


def save_data(ping, download, upload):
    path = os.environ['MODULE_PATH'] + '/runtime/data.csv'
    test_time = time.localtime()
    ping_to_save = ping
    download_to_save = download
    upload_to_save = upload
    with open(path, 'a') as data_file:
        data_file.write(f'{test_time[2]:02}-{test_time[1]:02}-{test_time[0]:04} '
                        f'{test_time[3]:02}:{test_time[4]:02}:{test_time[5]:02};{ping_to_save};'
                        f'{download_to_save};{upload_to_save}\n')


def clear_data_file():
    path = os.environ['MODULE_PATH'] + '/runtime'
    for file in os.listdir(path):
        os.remove(path + '/' + file)
    os.rmdir(os.environ['MODULE_PATH'] + '/runtime')
