import os
import json
import numpy as np
import random
import re
import time

import serial

from typing import List

# 0    1    2    3    4    5    6    7    8    9    10   11   12    13    14
notes = [
    330, 370, 415, 440, 494, 554, 622, 659, 740, 831, 880, 988, 1109, 1245,
    1319
]
lengthNotes = len(notes)

main = [0, 2, 4, 7, 9, 11, 14]
lengthMains = len(main)

patterns = [[0], [-1, 0], [1, 0], [0, 1, 0], [0, -1, 0], [-1, 0, 1],
            [1, 0, -1]]
lengthPatterns = len(patterns)

min = [-24000, -24000, -24000, -24000, -24000, -24000, -24000]
max = [24000, 24000, 24000, 24000, 24000, 24000, 24000]

minDuration = 200
maxDuration = 1000


def beep(freq, dur=100):
    os.system('play -n synth %s sin %s' % (dur / 1000, freq))


def split_text(s) -> List[int]:
    spl_txt_list = s.decode("utf-8").replace("\n", "").split(" ")
    return list(
        map(lambda x: float(spl_txt_list[x].replace("\n", "")),
            [2, 6, 10, 14, 18, 22, 26]))


filtered = np.zeros(7)
previous = np.zeros(7)
arduino = serial.Serial("/dev/cu.HC-05-DevB", timeout=1)
while True:

    arduino.reset_input_buffer()
    arduino.readline()
    d = split_text(arduino.readline())
    for i in range(len(d)):
        if d[i] > max[i]:
            d[i] = max[i]
        elif d[i] < min[i]:
            d[i] = min[i]
    patternIdx = int((d[0] - min[0]) / (max[0] - min[0]) * lengthPatterns)
    patternIdx %= len(patterns)
    pattern = patterns[patternIdx]

    if filtered[1] <= min[1]:
        mainNote = 0
    elif filtered[1] >= max[1]:
        mainNote = lengthMains - 1
    else:
        mainNote = (filtered[0] - min[1]) / (max[1] - min[1])
        mainNote = int(mainNote * lengthMains)

    gmax = np.max([np.abs(d[4]), np.abs(d[5]), np.abs(d[6])])
    duration = int((gmax / max[4]) * (maxDuration - minDuration) + minDuration)

    for i in range(len(pattern)):
        idx = (mainNote + pattern[i]) % lengthNotes
        beep(notes[idx], duration)
