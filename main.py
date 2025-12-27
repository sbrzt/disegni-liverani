# main.py

import pandas as pd
from src.extract import request_data , get_ids, extract_values, to_csv
from src.merge import merge_columns
from src.tainacan_prep import data_prep, download_images
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
    resp = request_data(ids, API_ENDPOINT, BATCH)
    data = extract_values(resp)
    download_images(pd.DataFrame(data))
    return to_csv(data), merge_columns(API_OUTPUT, DATASET_MANUAL, COLUMNS, KEY), data_prep(OUTPUT_ARCHIVE)


if __name__ == "__main__":
    main()
