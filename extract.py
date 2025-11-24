# extract.py

import requests

def get_ids(file):
    with open(file) as f:
        ids_str = f.read()
        ids = ids_str.strip().split("\n")
    return ids


def extract_data(ids, endpoint, batch):
    data = []
    for i in range(0, len(ids), batch):
        req_str = ",".join(ids[i:i+batch])
        req = endpoint + req_str
        resp = requests.get(req)
        data.append(resp.text)
    return data
