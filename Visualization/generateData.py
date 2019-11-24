import time
import json
import random

date = 1574524425
while(True):
    date += 1
    r = random.randint(3000, 15000)
    with open("data.json", "r") as read_file:
        data = json.load(read_file)
        data['raw_data'].append(
            [date, -1636.0 + r, 10704.0 - r, 2148.0 + r, 27.07 + r, -18639.0 - r, -12236.0 + r, -32768.0 - r])
    with open("data.json", 'w') as f:
        json.dump(data, f)
    time.sleep(2)
