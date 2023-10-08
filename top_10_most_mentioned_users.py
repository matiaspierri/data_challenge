import pandas as pd
import json
#from memory_profiler import profile

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


# Drop rows with None or NaN values in the "mentionedUsers" column
# We only want to keep users that were mentioned
df.dropna(subset=['mentionedUsers'], inplace=True)

df['usernameMentionedList'] = df['mentionedUsers'].apply(lambda user_list: [user['username'] for user in user_list if 'username' in user])

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
sorted_username_tuples[:10]