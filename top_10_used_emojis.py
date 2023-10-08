import pandas as pd
import json
import cProfile
import emoji
from memory_profiler import profile


# Define a function to extract emojis from a string using the emoji module
def extract_emojis(text):
    return ''.join(char for char in text if emoji.is_emoji(char))

