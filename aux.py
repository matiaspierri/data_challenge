import pandas as pd
import json

def load_JSON_into_df(file_path: str):
    
    data= []
    invalid_rows= []

    missing_rows = 0

    # Try to read the JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read and parse each line separately
        for row in file:
            try:
                jsonparse = json.loads(row)
                data.append(jsonparse)
            except Exception as e:
                missing_rows +=1
                invalid_rows.append(row)

    print(f'Missing rows: {missing_rows}')
    print(f'Invalid rows: {invalid_rows}')

    return pd.DataFrame(data)