import json
import os
import re
import time

import serial
from flask import Flask, stream_with_context, Response
from typing import List

app = Flask(__name__)

arduino = serial.Serial("/dev/cu.HC-05-DevB", timeout=1)

notes = [262, 294, 330, 392, 440, 523, 587, 659, 784, 880]
length = len(notes)

filtered = 0.0

min = -30000
max = 27000


def beep(freq, dur=100):
    os.system('play -n synth %s sin %s' % (dur / 1000, freq))


def split_text(s) -> List[int]:
    spl_txt_list = s.decode("utf-8").replace("\n", "").split(" ")
    return list(
        map(lambda x: float(spl_txt_list[x].replace("\n", "")),
            [2, 6, 10, 14, 18, 22, 26]))


def generate():
    while True:
        global filtered
        lst = split_text(arduino.readline())
        js = {"raw_output": lst}
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
        yield json.dumps(js)


@app.route("/stream")
def stream():
    rows = generate()

    return Response(stream_with_context(rows))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
