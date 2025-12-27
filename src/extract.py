# src/extract.py

import requests
from jsonpath_ng.ext import parse
import json
from tqdm import tqdm
from config import (
    TARGET_VALUES, 
    IMAGE_PREFIX, 
    API_OUTPUT
)
import pandas as pd
from src.merge import merge_columns


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
    matches = jsonpath_expression.find(dct)
    if matches:
        values = []
        is_image_path = "FTAZ" in jsonpath_expr
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
        return values[0]
    return None


def extract_values(data):
    values = []
    for dct in tqdm(data):
        obj_values = {}
        for value in tqdm(TARGET_VALUES.values()):
            try:
                jsonpath_expr = value[2]
                obj_values[value[0]] = look_up(dct, jsonpath_expr)
            except:
                continue
        values.append(obj_values)
    return values


def to_csv(data):
    df = pd.DataFrame.from_dict(data)
    return df.to_csv(API_OUTPUT, index=False)