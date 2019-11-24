import json

import pandas as pd


def to_dataframe(js):
    ax = []
    ay = []
    az = []
    tmp = []
    gx = []
    gy = []
    gz = []
    for j in js:
        raw_data = j["raw_data"]
        ax.append(raw_data[0])
        ay.append(raw_data[1])
        az.append(raw_data[2])
        tmp.append(raw_data[3])
        gx.append(raw_data[4])
        gy.append(raw_data[5])
        gz.append(raw_data[6])
    return pd.DataFrame({
        "ax": ax,
        "ay": ay,
        "az": az,
        "gx": gx,
        "gy": gy,
        "gz": gz
    })


def concat(names):
    dfs = []
    for name in names:
        with open(f"{name}.json", "r") as f:
            data = json.load(f)
        df = to_dataframe(data)
        df["type"] = name
        dfs.append(df)
    return pd.concat(dfs, axis=0, sort=False).reset_index(drop=True)


if __name__ == "__main__":
    names = [
        "crawl", "handsover", "handsside", "handsup", "rotate", "twisting"
    ]
    dfs = concat(names)
    dfs.to_csv("all.csv", index=False)
