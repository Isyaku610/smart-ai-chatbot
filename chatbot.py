import os

MEMORY_FILE = "data/memory.txt"

def save_memory(key, value):
    data = {}

    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            for line in f:
                if "=" in line:
                    k, v = line.strip().split("=", 1)
                    data[k] = v

    data[key] = value

    with open(MEMORY_FILE, "w") as f:
        for k, v in data.items():
            f.write(f"{k}={v}\n")


def get_memory(key):
    if not os.path.exists(MEMORY_FILE):
        return None

    with open(MEMORY_FILE, "r") as f:
        for line in f:
            if "=" in line:
                k, v = line.strip().split("=", 1)
                if k == key:
                    return v

    return None
