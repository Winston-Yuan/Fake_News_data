import json
import re

# Function to normalize titles
def normalize_title(title):
    # Convert to lower case and remove non-alphanumeric characters except spaces
    return re.sub(r'[^a-zA-Z0-9\s]', '', title.lower())

# Load and normalize titles from the first dataset (Ti-CNN_title.json)
file_path_ti_cnn = 'Ti-CNN_title.json'
with open(file_path_ti_cnn, 'r', encoding='utf-8') as file:
    ti_cnn_titles = json.load(file)
normalized_ti_cnn = {key: normalize_title(title) for key, title in ti_cnn_titles.items()}

# Load and normalize titles from the second dataset (gossipcop_title.json)
file_path_gossipcop = 'gossipcop_title.json'
with open(file_path_gossipcop, 'r', encoding='utf-8') as file:
    gossipcop_titles = json.load(file)
normalized_gossipcop = {key: normalize_title(title) for key, title in gossipcop_titles.items()}

# Find duplicates
duplicates = {ti_key: ti_title for ti_key, ti_title in normalized_ti_cnn.items() if ti_title in normalized_gossipcop.values()}

# Output the duplicates
print(duplicates)
