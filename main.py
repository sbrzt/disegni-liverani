# main.py

from extract import request_data , get_ids, extract_values
from config import (
    API_ENDPOINT,
    FILE,
    BATCH
)


def main():
    try:
        ids = get_ids(FILE)
        data = request_data(ids, API_ENDPOINT, BATCH)
        print(extract_values(data))
    except:
        None


if __name__ == "__main__":
    main()
