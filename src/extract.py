# src/extract.py

import requests
from jsonpath_ng.ext import parse
from tqdm import tqdm
from config import (
    TARGET_VALUES, 
    IMAGE_PREFIX, 
    API_OUTPUT
)
import pandas as pd


COMPILED_PATHS = {}
for value in TARGET_VALUES.values():
    if "path" in value:
        COMPILED_PATHS[value["key"]] = parse(value["path"])


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


def look_up(dct, field_name, is_image_path):
    if field_name not in COMPILED_PATHS:
        return None
    matches = COMPILED_PATHS[field_name].find(dct)
    if matches:
        values = []
        for match in matches:
            val = match.value
            if isinstance(val, list):
                val = val[0] if val else ""
            if not isinstance(val, str):
                val = str(val) if val is not None else ""
            if val and is_image_path:
                val = IMAGE_PREFIX + val
            if val:
                values.append(val)
        return values[0] if values else None
    return None


def extract_values(data):
    values = []
    for dct in tqdm(data):
        obj_values = {}
        for value in tqdm(TARGET_VALUES.values()):
            field_name = value["key"]
            raw_path = value["path"] if "path" in value else ""
            if not raw_path:
                continue
            is_image = "FTAZ" in raw_path
            obj_values[field_name] = look_up(dct, field_name, is_image)
        values.append(obj_values)
    return values