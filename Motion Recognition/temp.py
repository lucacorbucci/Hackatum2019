import time
import re

import matplotlib.pyplot as plt
import serial

from typing import List

arduino = serial.Serial("/dev/cu.HC-05-DevB", timeout=1)

while True:
    print(arduino.readline().decode("utf-8").replace("\n", ""))
