import pandas as pd
import json
import cProfile
from memory_profiler import profile

@profile
def find_top_10_tweets_count_dates(file_path: str):
    # Specify the file path
    file_path = "farmers-protest-tweets-2021-2-4.json"

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

    # Create a DataFrame from the parsed data
    df = pd.DataFrame(data)

    # Removing hours, minutes and seconds
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%m-%d-%Y')
    
    # Extracting username information
    df['username'] = df['user'].apply(lambda x: x['username'])

    # Counting tweets aggregated by date + username
    top_users = df.groupby('date')['username'].value_counts().reset_index(name='record_count')
    
    # Sort the DataFrame by 'record_count' in descending order 
    top_users = top_users.sort_values(by=['date', 'record_count'], ascending=[True, False])

    # Top 10 dates and username with most tweets by that given date
    top10_users = top_users.groupby('date').max().reset_index().head(10)

    
    # Returning result in a tuple
    return [tuple(row[['date', 'username']]) for _, row in top10_users.iterrows()]


if __name__ == "__main__":
    # Create a cProfile object
    profiler = cProfile.Profile()
    

    
    # Run the function within the profiler
    profiler.enable()
    top_10_dates = find_top_10_tweets_count_dates("farmers-protest-tweets-2021-2-4.json")
    profiler.disable()
    
    # Print the profiling results
    profiler.print_stats(sort='cumulative')

    print(top_10_dates)


    