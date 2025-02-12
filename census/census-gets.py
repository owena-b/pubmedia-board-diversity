import csv
import config
from census import Census

inCSV = 'city_fips.csv'
outCSV = 'city_demos.csv'

varsList = ['NAME', 'B01003_001E', 'B02001_002E', 'B02001_003E', 'B02001_004E', 'B02001_005E', 'B02001_006E',
            'B02001_008E', 'B03003_003E']
headers = ['Place', 'Total', 'White alone', 'Black or African American alone', 'American Indian and Alaska Native alone',
           'Asian alone', 'Native Hawaiian and Other Pacific Islander alone', 'Multiracial', 'Hispanic or Latino']

locList = []

with open(inCSV, newline='') as inFile:
    rows = csv.reader(inFile)
    for row in rows:
        locList.append(row)
    locList.pop(0)

c = Census(key=config.API_KEY, year=2022)

response = ''

with open(outCSV, 'w', newline='', encoding='utf-8') as outFile:
    writer = csv.DictWriter(outFile, fieldnames=headers)
    writer.writeheader()
    for loc in locList:
        if loc[2] == 'ERROR':
            continue
        if loc[2] == 'place':
            response = c.acs5.state_place(varsList, loc[4], loc[3])[0]
        elif loc[2] == 'cousub':
            response = c.acs5.state_county_subdivision(varsList, loc[4], loc[5], loc[3])[0]
        elif loc[2] == 'state':
            response = c.acs5.state(varsList, loc[4])[0]

        if type(response) is dict and bool(response):  # check if it's a non-empty dictionary
            if loc[2] != 'state':
                name = loc[0] + ', ' + loc[1]
            else:
                name = "State of " + loc[1]
            total = int(response.get('B01003_001E'))
            white = int(response.get('B02001_002E'))
            black = int(response.get('B02001_003E'))
            native = int(response.get('B02001_004E'))
            asian = int(response.get('B02001_005E'))
            nhpi = int(response.get('B02001_006E'))
            multiracial = int(response.get('B02001_008E'))
            hispanic = int(response.get('B03003_003E'))

            writer.writerow({
                'Place': name,
                'Total': total,
                'White alone': white,
                'Black or African American alone': black,
                'American Indian and Alaska Native alone': native,
                'Asian alone': asian,
                'Native Hawaiian and Other Pacific Islander alone': nhpi,
                'Multiracial': multiracial,
                'Hispanic or Latino': hispanic
            })

