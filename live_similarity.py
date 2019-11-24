import os
import time
import re
import pickle

import serial
import numpy as np

from typing import List

from tslearn.metrics import dtw

# notes = [262, 294, 330, 349, 392, 440, 494, 523, 587]
notes = [262, 294, 330, 392, 440, 523, 587, 659, 784, 880]
length = len(notes)

min = -30000
max = 27000

filtered = 0.0


def beep(freq, dur=100):
    os.system('play -n synth %s sin %s' % (dur / 1000, freq))


def split_text(s) -> List[int]:
    spl_txt_list = s.decode("utf-8").replace("\n", "").split(" ")
    return list(
        map(lambda x: float(spl_txt_list[x].replace("\n", "")),
            [2, 6, 10, 14, 18, 22, 26]))


if __name__ == "__main__":
    arduino = serial.Serial("/dev/cu.HC-05-DevB", timeout=1)
    try:
        with open("scaler.pkl", "rb") as f:
            scaler = pickle.load(f)
        hist = [[] for _ in range(6)]

        rotate = []
        for name in ["ax", "ay", "az", "gx", "gy", "gz"]:
            with open(f"rotate/{name}.npy", "rb") as f:
                rotate.append(np.load(f))

        arduino.readline()
        while True:
            try:
                lst = split_text(arduino.readline())
            except ValueError or IndexError:
                continue
            lst = np.array(lst)[[0, 1, 2, 4, 5, 6]]
            if len(hist[0]) < 6:
                for i, x in enumerate(lst):
                    hist[i].append(x)
            else:
                for i, x in enumerate(hist):
                    x.reverse()
                    x.pop()
                    x.reverse()
                    x.append(lst[i])
                hist_np = scaler.transform(np.array(hist))
                rotate_np = np.zeros((6, 6))
                for i, arr in enumerate(rotate):
                    rotate_np[:, i] = arr
                rotate_np = scaler.transform(rotate)
                sims = []
                for i in range(6):
                    sims.append(dtw(hist_np[:, i], rotate_np[:, i]))
                print(np.mean(sims))

                if filtered <= min:
                    idx = 0
                elif filtered >= max:
                    idx = length - 1
                else:
                    idx = (filtered - min) / (max - min)
                    idx = int(idx * length)
                if np.mean(sims) > 4:
                    beep(notes[int(idx)], 100)
    except Exception:
        arduino.close()
        raise
