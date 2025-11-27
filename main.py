# main.py

from extract import request_data , get_ids, extract_values, to_csv
from config import (
    API_ENDPOINT,
    FILE,
    BATCH
)


def main():
    ids = get_ids(FILE)
    resp = request_data(ids, API_ENDPOINT, BATCH)
    data = extract_values(resp)
    return to_csv(data)


if __name__ == "__main__":
    main()
