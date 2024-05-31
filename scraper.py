import requests
import csv
from bs4 import BeautifulSoup
from fixes import state_fixes

URL = 'https://enterpriseefiling.fcc.gov/dataentry/public/form323/draftCopyForm323.html?displayType=html&appKey=25076ff38bd02040018bd90eb5de2332&id=25076ff38bd02040018bd90eb5de2332&goBack=N'

CSV_FILE = 'pubmedia-board-members-data.csv'

CSV_HEADERS = [
    'Licensee',
    'State',
    'Name',
    'Occupation',
    'Gender',
    'Ethnicity',
    'Race',
    'Voting Interest'
]

r = requests.get(URL)

sections = BeautifulSoup(r.text, 'html.parser').find_all('section')

# Takes the licensee's name from the first table at the top of the page.
licensee = str(sections[0].find_all('table')[0].find_all('td')[1].text.strip())

# Translates the state abbreviations into their full names.
state = state_fixes.get(str(sections[0].find_all('table')[1].find_all('td')[2].text.strip()))

# The 'tables' variable excludes the last table, which is a questionnaire about voting and equity interests.
tables = sections[6].find_all('table')[:-1]

with open(CSV_FILE, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=CSV_HEADERS)
    writer.writeheader()

    for table in tables:
        tbody = table.find('tbody')
        row = tbody.find_all('tr')

        # The first (and sometimes second) table in the section is the licensee or its parent entity. By identifying
        # the type of table, the program skips tables for entities and only collects data on humans.
        if row[1].find_all('td')[0].text.strip() == 'Entity Name':
            continue

        name = row[1].find_all('td')[1].text.strip()

        occupation = row[11].find_all('td')[1].text.strip()

        gender = row[15].find_all('td')[1].text.strip()

        ethnicity = row[16].find_all('td')[1].text.strip()

        race = row[17].find_all('td')[1].text.strip()

        voting = row[18].find_all('td')[2].text.strip()

        # Write the row
        writer.writerow({
            'Licensee': licensee,
            'State': state,
            'Name': name,
            'Occupation': occupation,
            'Gender': gender,
            'Ethnicity': ethnicity,
            'Race': race,
            'Voting Interest': voting
        })
