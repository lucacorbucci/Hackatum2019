import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler


def window(val: float, hist: np.ndarray):
    new_hist = hist[1:].tolist()
    new_hist.append(val)
    return np.array(new_hist)


def scale(hist: np.ndarray, scaler: StandardScaler):
    return scaler.transform(hist)


if __name__ == "__main__":
    all_data = pd.read_csv("all.csv")
    scalers = []
    for t in all_data["type"].unique():
        sub = all_data.query(f"type == '{t}'")
        subdrop = sub.drop("type", axis=1)
        scaler = StandardScaler()
        scaled = scaler.fit_transform(subdrop)
        scalers.append(scaled)
