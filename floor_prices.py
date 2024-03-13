
# floor prices: https://docs.blockspan.com/reference/getcollectionpricehistory
from dotenv import load_dotenv  # Import the load_dotenv function
import os  # Make sure you also import os

# Other imports remain the same
import requests
import json
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Now you can access the blockspan_key environment variable
blockspan_key = os.getenv('blockspan_key')

# Ensure the blockspan_key was loaded
if blockspan_key is None:
    raise ValueError("blockspan_key not found. Please make sure it's set in your .env file.")

# Define your input parameters here
contract_address = "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"
chain = "eth-main"
timeframe = "30_DAYS"
bin_size = "1_DAY"
timestamp_end = datetime.strptime("2023-03-10T00:00:00", '%Y-%m-%dT%H:%M:%S')

# Validate bin_size based on timeframe
valid_bin_sizes = {
    '1_DAY': ['15_MIN', '1_HOUR'],
    '7_DAYS': ['1_HOUR', '1_DAY'],
    '30_DAYS': ['1_DAY'],
}

if bin_size not in valid_bin_sizes[timeframe]:
    raise ValueError(f"Invalid bin_size '{bin_size}' for timeframe '{timeframe}'. Valid options are: {', '.join(valid_bin_sizes[timeframe])}.")

# Constructing the URL
url = f"https://api.blockspan.com/v1/collections/pricehistory/contract/{contract_address}?chain={chain}&timeframe={timeframe}&bin_size={bin_size}&timestamp_end={timestamp_end.strftime('%Y-%m-%dT%H:%M:%S')}"

headers = {
    "accept": "application/json",
    "X-API-KEY": blockspan_key 
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Use the json.loads() method to parse the response.text into a Python dictionary
    data = json.loads(response.text)

    # Pretty print the output using json.dumps(), with an indent of 4 spaces for better readability
    pretty_output = json.dumps(data, indent=4)

    print(pretty_output)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
