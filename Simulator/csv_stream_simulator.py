import pandas as pd
import json
import time

FILE_PATH = "D:\Projects\AtmoSync\Data\AtmoSync_Micro_Climate_Analytics_12000.csv"

df = pd.read_csv(FILE_PATH)

print(f"Loaded {len(df)} records")

for _, row in df.iterrows():

    record = row.to_dict()

    print(json.dumps(record, indent=2))

    time.sleep(1)
