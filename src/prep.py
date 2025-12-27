# src/tainacan_prep.py

import os
import requests
import pandas as pd
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from config import (
    TARGET_VALUES,
    LABEL_SEPARATOR,
    DB_KEY_PARAMETER,
    STATUS_PRIVATE_PARAMETER,
    STATUS_PUBLIC_PARAMETER,
    TEXT_PARAMETER,
    NUMERIC_PARAMETER,
    RELATIONSHIP_PARAMETER,
    OUTPUT_PUBLISH
)


def download_single(args):
    url, path = args
    if not url:
        return
    try:
        resp = requests.get(url, timeout=10)
        with open(path, "wb") as f:
            f.write(resp.content)
    except Exception as e:
        print(f"Error on {url}: {e}")

def download_images(data):
    ids = data[TARGET_VALUES[1]["key"]]
    verso_urls = data[TARGET_VALUES[25]["key"]].tolist()
    recto_urls = data[TARGET_VALUES[26]["key"]].tolist()
    img_dir = os.path.join('data','img')
    recto_dir = os.path.join('data','img', 'recto')
    verso_dir = os.path.join('data','img', 'verso')
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    if not os.path.exists(recto_dir):
        os.makedirs(recto_dir)
    if not os.path.exists(verso_dir):
        os.makedirs(verso_dir)
    
    tasks = []
    for i, url in enumerate(verso_urls):
        tasks.append((url, f'{verso_dir}/{ids[i]}-v.jpg'))
    for i, url in enumerate(recto_urls):
        tasks.append((url, f'{recto_dir}/{ids[i]}-r.jpg'))
    with ThreadPoolExecutor(max_workers=10) as executor:
        list(tqdm(executor.map(download_single, tasks), total=len(tasks)))


def data_prep(data):
    df = pd.read_csv(data)
    df["special_document"] = "file:disegni/" + df[TARGET_VALUES[1]["key"]].astype(str) + "-v.jpg"
    df["special_attachments"] = "disegni/" + df[TARGET_VALUES[1]["key"]].astype(str) + "-v.jpg; disegni/" + df[TARGET_VALUES[1]["key"]].astype(str) + "-r.jpg"
    rename_map = {}
    for conf in TARGET_VALUES.values():
        new_name = LABEL_SEPARATOR.join([
            conf["label"],
            conf["type"],
            conf["status"]
        ])
        rename_map[conf["key"]] = new_name
    df_2 = df.rename(columns=rename_map)
    return df_2.to_csv(OUTPUT_PUBLISH, index=False)