# extract.py

import requests
import json
from tqdm import tqdm
from config import TARGET_VALUES

def get_ids(file):
    with open(file) as f:
        ids_str = f.read()
        ids = ids_str.strip().split("\n")
    return ids


def request_data(ids, endpoint, batch):
    data = []
    for i in tqdm(range(0, len(ids), batch)):
        req_str = ",".join(ids[i:i+batch])
        req = endpoint + req_str
        resp = requests.get(req, timeout=10)
        batch_data = resp.json()
        data.extend(batch_data)
    return data


def extract_values(data):
    values = []
    for dct in data:
        obj_values = {}
        obj_values["type"] = eval(TARGET_VALUES["type"])
        obj_values["subject"] = eval(TARGET_VALUES["subject"])
        obj_values["place"] = f"{eval(TARGET_VALUES['province'])} ({eval(TARGET_VALUES['place'])}), {eval(TARGET_VALUES['nation'])}"
        
        
        values.append(obj_values)
    for value in values:
        print(value)


