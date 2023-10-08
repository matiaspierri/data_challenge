import pandas as pd
import json
import cProfile
from memory_profiler import profile

def load_JSON_into_df():
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

    return pd.DataFrame(data)

@profile
def find_top_10_most_mentioned_users(file_path: str):

    

    # Create a DataFrame from the parsed data
    df = load_JSON_into_df()

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
    profiler.print_stats(sort='cumulative')

    print(top_10_mentioned_users)