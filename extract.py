# extract.py

import requests
from jsonpath_ng.ext import parse
import json
from tqdm import tqdm
from config import TARGET_VALUES, IMAGE_URL


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


def look_up(dct, jsonpath_expr):
    jsonpath_expression = parse(jsonpath_expr)
    match = jsonpath_expression.find(dct)
    if match:
        val = match[0].value
        if isinstance(val, list):
            return " ".join(val)
        return str(val)
    return None


def extract_values(data):
    values = []
    for dct in data:
        obj_values = {}
        for key, jsonpath_expr in tqdm(TARGET_VALUES.items()):
            obj_values[key] = look_up(dct, jsonpath_expr)        
        values.append(obj_values)
        print(obj_values)
    return values