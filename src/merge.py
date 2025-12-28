# src/merge.py

import pandas as pd
from config import (
    OUTPUT_ARCHIVE
)


def merge_columns(dataset_1, dataset_2, columns, key):
    """
    Merges two CSV datasets on a common key and saves the result, by
    performing an inner join on a set of specific columns.

    Args:
        dataset_1 (str): Path to the primary CSV file (e.g., API extracted data).
        dataset_2 (str): Path to the secondary CSV file containing manual data.
        columns (list[str]): List of column names to import from dataset_2.
        key (str): The column name to use as the join key.

    Returns:
        None
    """
    df_1 = pd.read_csv(dataset_1)
    df_2 = pd.read_csv(dataset_2, usecols=columns)
    df_1[key] = df_1[key].astype(str)
    df_2[key] = df_2[key].dropna().astype(int).astype(str)
    merged = df_1.merge(df_2, how="inner", on=key)
    merged = merged.drop_duplicates(subset=[key])
    merged.to_csv(OUTPUT_ARCHIVE, index=False)