import os
import pandas as pd

def load_csv ( file_path ):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found in data folder")
    df = pd.read_csv(file_path)

    df.columns = df.columns.str.strip().str.lower()

    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')  # strings → numbers, errors → NaN

    df = df.dropna(subset=['amount'])
    return df

# Test the loader
if __name__ == "__main__":
    csv_path = "../data/sales.csv"
    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} rows from {csv_path}")
    print(df.head(10))
    print("Columns in CSV:", df.columns.tolist())


