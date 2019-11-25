import json

if __name__ == "__main__":
    with open("sample.json", "r") as f:
        data = json.load(f)

    new = []
    for d in data:
        new.append([d["time"]] + d["raw_data"])
    dct = {"raw_data": new}
    with open("new_sample.json", "w") as f:
        json.dump(dct, f)
