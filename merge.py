# This script merges two CSV files matching the rows by the id and adding the columns from the first csv to the second  one. The merged output is saved as 'merged.csv'.
import pandas as pd
import argparse

def merge_csv_files(csv_1, csv_2, merge_columns, id, output):
    # Merge csv_1 into csv_2 by 'id'
    try:
        csv1_df = pd.read_csv(csv_1)
        csv2_df = pd.read_csv(csv_2)

        print("Successfully loaded both CSV files.")

        for col in merge_columns:
            possible_col = [c for c in csv1_df.columns if c.lower()==col]
            # Every column must be found
            if not possible_col:
                raise KeyError(f"Column '{col}' not found in {csv_1}")
            

        if id not in csv1_df.columns or id not in csv2_df.columns:
            raise KeyError(f"{id} column missing in one of the files")
        
        print(f"Merging columns {merge_columns} from {csv_1} into {csv_2} based on '{id}' column.")
        cols = list(merge_columns)+[id]
        subs = csv1_df[cols]

        print ("Merging data...")
        merged_df = pd.merge(csv2_df, subs, on=id, how='left')

        merged_df.to_csv(output, index=False)
        print(f"\nSuccessfully merged files! Saved to {output}")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    description="Merge csv_1 with one dataset and csv_2 with another dataset by an identifier_column header and appends any columns that have the header present in the list merge_columns to csv_2.")
    parser.add_argument("csv_1", help="Path to csv_1 CSV (contains identifier_column and merge_columns headers)")
    parser.add_argument("csv_2", help="Path to csv_2 CSV (contains identifier_column header)")
    parser.add_argument("--merge_columns", nargs="+", required=True, help="Columns to merge from csv_1 to csv_2 (e.g., latitude longitude)")
    
    parser.add_argument("-id", "--identifier_column", default="id", help="Identifier column header (default: id)")
    parser.add_argument("-o", "--output", default="merged.csv", help="Output CSV path (default: merged.csv)")

    args = parser.parse_args()
    merge_csv_files(args.csv_1, args.csv_2, args.merge_columns, args.identifier_column, args.output)