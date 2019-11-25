import os
import time
import re

import serial

from typing import List

# notes = [262, 294, 330, 349, 392, 440, 494, 523, 587]
notes = [262, 294, 330, 392, 440, 523, 587, 659, 784, 880]
length = len(notes)

min = -30000
max = 27000

filtered = 0.0


def beep(freq, dur=100):
    os.system('play -n synth %s sin %s' % (dur / 1000, freq))


arduino = serial.Serial("/dev/cu.HC-05-DevB", timeout=1)


def split_text(s) -> List[int]:
    spl_txt_list = s.decode("utf-8").replace("\n", "").split(" ")
    return list(
        map(lambda x: float(spl_txt_list[x].replace("\n", "")),
            [2, 6, 10, 14, 18, 22, 26]))


if __name__ == "__main__":
    arduino = serial.Serial("/dev/cu.HC-05-DevB", timeout=1)

    arduino.readline()
    while True:
        lst = split_text(arduino.readline())
        x = lst[5]
        filtered = 0.2 * filtered + 0.8 * x
        if filtered <= min:
            idx = 0
        elif filtered >= max:
            idx = length - 1
        else:
            idx = (filtered - min) / (max - min)
            idx = int(idx * length)

        beep(notes[int(idx)], 300)
