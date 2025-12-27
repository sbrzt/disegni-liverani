# src/merge.py

import pandas as pd
from config import (
    OUTPUT_ARCHIVE
)


def merge_columns(dataset_1, dataset_2, columns, key):
    df_1 = pd.read_csv(dataset_1)
    df_2 = pd.read_csv(dataset_2)
    df_columns = df_2[columns].copy()
    df_1[key] = df_1[key].astype(str)
    df_columns[key] = df_columns[key].dropna().astype(int).astype(str)
    merged = df_1.merge(df_columns, how="left", on=key)
    return merged.to_csv(OUTPUT_ARCHIVE, index=False)