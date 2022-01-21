# SpeedTestTracking

Provides a way to constantly monitor network performance. It collects network speeds over a long time and plots the results to be easily accessible.

## Installation

Just download the correct executable from the [release](https://github.com/MatteoH2O1999/SpeedTestTracking/releases) section. The cli interface is faster, occupies less resources and is designed to be run in the background. The GUI interface is based on Chromium (don't worry, if you have Chrome it will work) and is more resource-heavy but it will provide real-time feedback.

## Usage

The GUI will start with a form for you to fill with the requiered parameters. The CLI executable may be called with the parameters as command line arguments. If no parameters are given, you will be prompted to enter only the required ones.
Parameters should be given with the following format:  
`executable-cli TIME-BETWEEN-TEST SAVE-PLOT-TO [MAX-PLOT-TICKS]`

Both executables may take a while to load. DO NOT PANIC, thats normal.
