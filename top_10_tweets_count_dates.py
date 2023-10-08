import pandas as pd
import json
import cProfile
from aux import load_JSON_into_df
from memory_profiler import profile

@profile
def find_top_10_tweets_count_dates(file_path: str) -> List[Tuple[str, int]]:
    
    # Create a DataFrame from the parsed data
    df = load_JSON_into_df(file_path)

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
    #profiler.print_stats(sort='cumulative')

    print(top_10_dates)


    