import json
import os

def save_round(holes, filename):
    data = [hole.__dict__ for hole in holes]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_round(filename):
    with open(filename, "r") as f:
        return json.load(f)

def list_round_files():
    return [f for f in os.listdir() if f.startswith("runde_") and f.endswith(".json")]