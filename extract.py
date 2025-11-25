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
        obj_values["place"] = f"{eval(TARGET_VALUES['region'])} ({eval(TARGET_VALUES['province'])}), {eval(TARGET_VALUES['nation'])}"
        obj_values["conservation_org"] = eval(TARGET_VALUES["conservation_org"])
        obj_values["collection"] = eval(TARGET_VALUES["collection"])
        obj_values["inventory_id"] = eval(TARGET_VALUES["inventory_id"])
        obj_values["begin_date"] = eval(TARGET_VALUES["begin_date"])
        
        #obj_values["date"] = f"{eval(TARGET_VALUES['begin_date'])}-{eval(TARGET_VALUES['end_date'])}"
        
        obj_values["author"] = eval(TARGET_VALUES["author"])
        obj_values["measure_height"] = eval(TARGET_VALUES["measure_height"])
        obj_values["measure_length"] = eval(TARGET_VALUES["measure_length"])
        obj_values["measure_unit"] = eval(TARGET_VALUES["measure_unit"])
        
        
        values.append(obj_values)
    for value in values:
        print(value)


