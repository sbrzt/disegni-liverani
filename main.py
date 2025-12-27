# main.py

import pandas as pd
from src.extract import request_data , get_ids, extract_values
from src.merge import merge_columns
from src.prep import data_prep, download_images
from config import (
    API_ENDPOINT,
    ID_LIST,
    BATCH, 
    API_OUTPUT,
    DATASET_MANUAL,
    COLUMNS,
    KEY,
    OUTPUT_ARCHIVE
)


def main():
    ids = get_ids(ID_LIST)
    if not ids:
        return
    resp = request_data(ids, API_ENDPOINT, BATCH)
    data = extract_values(resp)
    df = pd.DataFrame(data)
    df.to_csv(API_OUTPUT, index=False)
    download_images(df)
    merge_columns(API_OUTPUT, DATASET_MANUAL, COLUMNS, KEY)
    data_prep(OUTPUT_ARCHIVE) 


if __name__ == "__main__":
    main()
