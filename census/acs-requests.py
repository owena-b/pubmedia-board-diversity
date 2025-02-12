import requests
import config

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
    'key': config.API_KEY
}

# Make the API request
response = requests.get(base_url, params=params)
data = response.text

print(data)
