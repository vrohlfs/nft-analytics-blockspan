
# top 10 collections + price: https://docs.blockspan.com/reference/gettopnfts
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
chain = "eth-main"
timeframe = "1_DAY"
timestamp_end = datetime.strptime("2023-03-10T00:00:00", '%Y-%m-%dT%H:%M:%S')
contract_address = "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"
# price_start = 0
# price_end = 200
include_nft_details = "false"
exclude_dex = "false"
#cursor = ""
page_size = 25

# Constructing the URL
url = f"https://api.blockspan.com/v1/nfts/topnfts?chain={chain}&timeframe={timeframe}&include_nft_details={include_nft_details}&exclude_dex={exclude_dex}&page_size={page_size}"

headers = {
    "accept": "application/json",
    "X-API-KEY": blockspan_key # This can be found after installing on your QuickNode endpoint this add-on:  https://marketplace.quicknode.com/add-on/nft-api-with-cached-metadata
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
