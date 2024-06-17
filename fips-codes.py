import requests
import pandas as pd

# Replace with your actual API key
api_key = '82d15734a7d6fa98f0968b97f19fdcf6052009b6'

# Base URL for the API
base_url = 'https://api.census.gov/data/2022/acs/acs5'

# Define parameters for the API call
params = {
    'get': 'NAME,PLACE',
    'for': 'place:*',
    'key': api_key
}

# Make the API request
response = requests.get(base_url, params=params)
data = response.json()

# Convert the data to a pandas DataFrame
columns = data[0]
rows = data[1:]
places_df = pd.DataFrame(rows, columns=columns)

# Save the DataFrame to a CSV file for future use
places_df.to_csv('us_places_fips.csv', index=False)

# Display the DataFrame
places_df.head()
