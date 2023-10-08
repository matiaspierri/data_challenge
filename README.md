# data_challenge

## Description
This repository has 3 python scripts. Each of these scripts answers a business questions about Tweeter(X) information.
- top_10_tweets_count_dates: The top 10 dates with the most tweets. Mention the user (username) with the most posts for each of those days. This script returns the following data type: List[Tuple[datetime.date, str]]
- top_10_used_emojis: The top 10 most used emojis with their respective counts. This script returns the following data type: List[Tuple[str, int]]
- top_10_most_mentioned_users: The historical top 10 most influential users (username) based on the count of mentions (@) each of them registers. This script returns the following data type: List[Tuple[str, int]]

## Installation

### Pre requesites

Make sure you have the following prerequisites installed on your system:
- Python 3.9
- pip (Python package manager)

### Step 1: Clone the Repository
Clone the repository to your local machine using the following command:

`git clone https://github.com/matiaspierri/data_challenge.git`

### Step 2: Create a Virtual Environment (Optional but Recommended)
It's a good practice to create a virtual environment to isolate the project dependencies. Navigate to the project directory and run the following commands:
```
# Create a virtual environment
python3.9 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On macOS and Linux
venv\Scripts\activate  # On Windows
```
### Step 3: Install Required Packages
With the virtual environment activated, install the required packages from the requirements.txt file using pip:
`pip install -r requirements.txt`
This will install the necessary packages, including pandas, emoji, and memory_profiler.

### Step 4: Run the Python Code
You can now run the Python code by executing the following command:

`python3 top_10_tweets_count_dates.py`

`python3 top_10_used_emojis.py`

`python3 top_10_most_mentioned_users.py`

### Step 5: Deactivate the Virtual Environment (Optional)
When you're done using the project, you can deactivate the virtual environment using the following command:

`deactivate`


