import json
import re
import time

import serial
from flask import Flask, stream_with_context, Response
from typing import List

app = Flask(__name__)

arduino = serial.Serial("/dev/cu.HC-05-DevB", timeout=1)


def split_text(s) -> List[int]:
    spl_txt_list = s.decode("utf-8").replace("\n", "").split(" ")
    return list(
        map(lambda x: float(spl_txt_list[x].replace("\n", "")),
            [2, 6, 10, 14, 18, 22, 26]))


def generate():
    while True:
        lst = split_text(arduino.readline())
        js = {"raw_output": lst}
        yield json.dumps(js)


@app.route("/stream")
def stream():
    rows = generate()

    return Response(stream_with_context(rows))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
