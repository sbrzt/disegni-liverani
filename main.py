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
    """
    Orchestrates the main processing workflow.

    This function performs the following sequential steps:
    1.  **Extraction**: Retrieves IDs from the configured source file and fetches
        JSON data from the API in batches.
    2.  **Storage**: Extracts specific fields based on the configuration file, converts
        them to a DataFrame, and saves the raw intermediate CSV.
    3.  **Assets**: Downloads images associated with the records to the local storage.
    4.  **Enrichment**: Merges the raw API data with the manual dataset
        preserving only specified columns.
    5.  **Formatting**: Transfroms the merged dataset into the final format required
        for import.

    Returns:
        None
    """
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
