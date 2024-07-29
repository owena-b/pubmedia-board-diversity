import requests

# Replace with your actual API key
api_key = '82d15734a7d6fa98f0968b97f19fdcf6052009b6'

# List of specific cities by FIPS code
fips_codes = {
    'West Tisbury, Massachusetts': '78235'
}

# Build the API request URL
base_url = 'https://api.census.gov/data/2020/acs/acs5'
params = {
    'get': 'NAME,B02001_007E,B02001_008E,B02001_009E',
    'for': 'place:38250',
    'in': 'state:47',
    'key': api_key
}

# Make the API request
response = requests.get(base_url, params=params)
data = response.text

print(data)
