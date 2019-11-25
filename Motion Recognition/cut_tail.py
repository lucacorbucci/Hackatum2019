import argparse
import json

import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

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
    plt.figure(figsize=(10, 5))
    cuts = []
    for i in range(7):
        cuts.append(arrays[i][-6:])
    ti = times[-6:]
    for i, arr in enumerate(cuts):
        plt.subplot(7, 1, i + 1)
        plt.plot(ti, arr, linewidth=2, color=colors[i])
    plt.savefig(f"{args.name}_cut.png")

    save_dir = Path(f"{args.name}")
    save_dir.mkdir(parents=True, exist_ok=True)
    names = ["ax", "ay", "az", "tmp", "gx", "gy", "gz"]
    for arr, name in zip(cuts, names):
        np.save(save_dir / f"{name}.npy", np.array(arr))
