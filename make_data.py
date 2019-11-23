import json
import time
import re

import serial

from typing import List

arduino = serial.Serial("/dev/cu.HC-05-DevB", timeout=1)


def split_text(s) -> List[int]:
    spl_txt_list = s.decode("utf-8").replace("\n", "").split(" ")
    return list(
        map(lambda x: float(spl_txt_list[x].replace("\n", "")),
            [2, 6, 10, 14, 18, 22, 26]))


arduino.readline()
t0 = time.time()
times = []
raw_datas = []
elapsed = time.time() - t0
while elapsed <= 50:
    lst = split_text(arduino.readline())
    times.append(time.time())
    raw_datas.append(lst)
    elapsed = time.time() - t0
    time.sleep(0.01)

js = []
for ti, raw in zip(times, raw_datas):
    dct = {}
    dct["time"] = ti
    dct["raw_data"] = raw
    js.append(dct)

with open("sample.json", "w") as f:
    json.dump(js, f)
