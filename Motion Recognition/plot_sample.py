import argparse
import json

import matplotlib.pyplot as plt

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    args = parser.parse_args()
    with open(f"{args.name}.json", "r") as f:
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
    plt.savefig(f"{args.name}.png")
