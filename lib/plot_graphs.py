# Plots the graphs once the tests are over. Works with a csv file.
import os

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from . import get_max_ticks


def plot(path, fast=False):
    os.makedirs(path, exist_ok=True)
    resolution = 1200
    if fast:
        resolution = 200
    max_ticks = get_max_ticks()
    plt.switch_backend('agg')
    file = os.environ['MODULE_PATH'] + '/runtime/data.csv'
    data = pd.read_csv(file, sep=';', index_col='time')
    labels = list(data.index.values)
    labels.sort()
    i = 0
    x_labels = labels
    while len(x_labels) > max_ticks:
        x_labels = []
        count = i
        for label in labels:
            if count == i:
                x_labels.append(label)
                count = 0
            else:
                count += 1
        i += 1
    sns.set_theme()
    sns.set_palette('colorblind')
    plt.figure(dpi=resolution)
    sns.lineplot(data=data, x='time', y='ping')
    plt.xlabel(None)
    plt.xticks(x_labels)
    plt.ylabel('Ping (ms)')
    plt.ylim(0, max(data['ping']) * 1.05)
    plt.xticks(rotation=20, horizontalalignment='right')
    plt.title('Ping')
    plt.savefig(path + '/ping.png', backend='agg', bbox_inches='tight')
    plt.clf()
    sns.lineplot(data=data, x='time', y='download')
    plt.xlabel(None)
    plt.xticks(x_labels)
    plt.ylabel('Download (Mbit/s)')
    plt.ylim(0, max(data['download']) * 1.05)
    plt.xticks(rotation=20, horizontalalignment='right')
    plt.title('Download')
    plt.savefig(path + '/download.png', backend='agg', bbox_inches='tight')
    plt.clf()
    sns.lineplot(data=data, x='time', y='upload')
    plt.xlabel(None)
    plt.xticks(x_labels)
    plt.ylabel('Upload (Mbit/s)')
    plt.ylim(0, max(data['upload']) * 1.05)
    plt.xticks(rotation=20, horizontalalignment='right')
    plt.title('Upload')
    plt.savefig(path + '/upload.png', backend='agg', bbox_inches='tight')
    data.to_excel(path + '/data.xlsx')
