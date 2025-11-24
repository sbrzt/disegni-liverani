# main.py

from extract import extract_data , get_ids
from config import (
    API_ENDPOINT,
    FILE,
    BATCH
)


def main():
    try:
        ids = get_ids(FILE)
        print(extract_data(ids, API_ENDPOINT, BATCH))
    except:
        None


if __name__ == "__main__":
    main()
