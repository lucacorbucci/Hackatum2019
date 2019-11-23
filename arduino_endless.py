import time
import re

import matplotlib.pyplot as plt
import serial

from typing import List

arduino = serial.Serial("/dev/cu.HC-05-DevB", timeout=1)


def split_text(s) -> List[int]:
    spl_txt_list = s.decode("utf-8").replace("\n", "").split(" ")
    return list(
        map(lambda x: float(spl_txt_list[x].replace("\n", "")),
            [2, 6, 10, 14, 18, 22, 26]))


plt.axis([0, 10, 0, 1])
plt.ylim(-50000, 50000)

colors = ["red", "green", "blue", "orange", "purple", "yellow", "black"]

arduino.readline()
while True:
    lst = split_text(arduino.readline())
    t0 = time.time()
    for i, l in enumerate(lst):
        plt.subplot(7, 1, i + 1)
        plt.scatter(t0, l, color=colors[i])
        plt.xlim(t0 - 20, t0 + 5)
    plt.pause(0.01)
