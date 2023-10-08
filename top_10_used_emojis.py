import pandas as pd
import json
import cProfile
import emoji
from memory_profiler import profile


# Define a function to extract emojis from a string using the emoji module
def extract_emojis(text):
    return ''.join(char for char in text if emoji.is_emoji(char))


# Apply the extract_emojis function to the "content" column
df['emojis'] = df['content'].apply(extract_emojis)

# Transforming all emojis coming from tweets in just one line
emojis_extracted = df['emojis'].str.cat()

# Dict to save emoji + count
emj_count = {}

# Iterate through the emojis
for emj in emojis_extracted:
    
    # If emoji is not in the dictionary, add it with a count of 1
    if emj not in emj_count:
        emj_count[emj] = 1
    # If the emoji is already in the dictionary, increment its count
    else:
        emj_count[emj] += 1

# Convert the dictionary to a list of tuples (emoji, count)
emj_count_tuple = [(emj, count) for emj, count in emj_count.items()]

# Sort the list of tuples by count in descending order
sorted_tuples = sorted(emj_count_tuple, key=lambda x: x[1], reverse=True)

# Return the sorted list of tuples as a tuple
tuple(sorted_tuples)