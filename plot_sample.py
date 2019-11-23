import json

import matplotlib.pyplot as plt

if __name__ == "__main__":
    with open("sample.json", "r") as f:
        data = json.load(f)

    arrays = [[] for _ in range(7)]
    times = []
    for d in data:
        times.append(d["time"])
        raw = d["raw_data"]
        for i, dd in enumerate(raw):
            arrays[i].append(dd)

    colors = ["red", "green", "blue", "orange", "yellow", "purple", "black"]
    plt.figure(figsize=(20, 15))
    for i, arr in enumerate(arrays):
        plt.subplot(7, 1, i + 1)
        plt.plot(times, arr, linewidth=2, color=colors[i])
    plt.savefig("sample.png")
