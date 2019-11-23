import os
import json

play = True

# notes = [262, 294, 330, 349, 392, 440, 494, 523, 587]
notes = [262, 294, 330, 392, 440, 523, 587, 659, 784, 880]
length = len(notes)

min = -30000
max = 27000

filtered = 0.0


def beep(freq, dur=100):
    os.system('play -n synth %s sin %s' % (dur / 1000, freq))


with open("sample.json") as json_file:
    data = json.load(json_file)
    for d in data:
        x = d["raw_data"][5]
        filtered = 0.5 * filtered + 0.5 * int(x)
        if filtered <= min:
            idx = 0
        elif filtered >= max:
            idx = length - 1
        else:
            idx = (filtered - min) / (max - min)
            idx = int(idx * length)
        print(idx)
        beep(notes[int(idx)], 200)
