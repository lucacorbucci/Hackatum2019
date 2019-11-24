import pickle
import pandas as pd

from sklearn.preprocessing import StandardScaler

if __name__ == "__main__":
    data = pd.read_csv("all.csv")
    data.drop("type", axis=1, inplace=True)
    scaler = StandardScaler()
    scaler.fit(data)
    with open("scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)
