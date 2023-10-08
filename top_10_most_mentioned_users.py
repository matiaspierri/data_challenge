import pandas as pd
import json
import cProfile
from aux import load_JSON_into_df
from memory_profiler import profile
from typing import List, Tuple

@profile
def find_top_10_most_mentioned_users(file_path: str) -> List[Tuple[str, int]]:

    # Create a DataFrame from the parsed data
    df = load_JSON_into_df(file_path)

    # Drop rows with None or NaN values in the "mentionedUsers" column
    # We only want to keep users that were mentioned
    df.dropna(subset=['mentionedUsers'], inplace=True)

    df['usernameMentionedList'] = df['mentionedUsers'].apply(lambda user_list: [user['username'] for user in user_list if 'username' in user])

    username_mentioned_plain_string = ' '.join(' '.join(username_list) for username_list in df['usernameMentionedList'])

    # Create a dictionary that contains the count of each username
    username_mention_count = {}

    for username in username_mentioned_plain_string.split():
        if username in username_mention_count:
            username_mention_count[username] += 1
        else:
            username_mention_count[username] = 1

    # Transform the dictionary into a list of tuples, ordered by descending count
    sorted_username_tuples = sorted(username_mention_count.items(), key=lambda x: x[1], reverse=True)

    # Keep only top 10
    return tuple(sorted_username_tuples[:10])

if __name__ == "__main__":
    # Create a cProfile object
    profiler = cProfile.Profile()
    
    # Run the function within the profiler
    profiler.enable()
    top_10_mentioned_users = find_top_10_most_mentioned_users("farmers-protest-tweets-2021-2-4.json")
    profiler.disable()
    
    # Print the profiling results
    #profiler.print_stats(sort='cumulative')

    print(top_10_mentioned_users)