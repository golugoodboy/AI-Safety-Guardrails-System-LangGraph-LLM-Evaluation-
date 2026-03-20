import json
import os 
from datetime import datetime

logs_file = "logs.jsonl"

def log_result(data : dict):
    log_entry = {
        "timestamp" : datetime.now().isoformat(),
        "data" : data
    }

    with open(logs_file, "a") as f:
        json.dump(log_entry, f)
        f.write("\n")

if __name__ == "__main__":
    pass



