import requests
import pandas as pd

# Replace with your actual API key
api_key = '82d15734a7d6fa98f0968b97f19fdcf6052009b6'

# List of specific cities by FIPS code
fips_codes = {
    'West Tisbury, Massachusetts': '78235'
}

# Build the API request URL
base_url = 'https://api.census.gov/data/2020/acs/acs5'
params = {
    'get': 'NAME,B02001_002E,B02001_003E,B02001_004E,B02001_005E,B02001_006E,B02001_007E,B02001_008E,B03001_003E',
    'for': 'place:' + ','.join(fips_codes.values()),
    'key': api_key
}

# Make the API request
response = requests.get(base_url, params=params)
data = response.json()

# Convert the data to a pandas DataFrame
columns = data[0]
rows = data[1:]
df = pd.DataFrame(rows, columns=columns)

# Rename the columns for readability
df.columns = ['City', 'White', 'Black or African American', 'American Indian and Alaska Native', 'Asian',
              'Native Hawaiian and Other Pacific Islander', 'Some other race', 'Two or more races', 'Hispanic or Latino']

# Convert data types to appropriate types
for col in df.columns[1:]:
    df[col] = df[col].astype(int)

# Display the DataFrame
print(df)
