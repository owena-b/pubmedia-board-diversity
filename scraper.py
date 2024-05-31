import requests
import csv
from bs4 import BeautifulSoup
from fixes import state_fixes

URLS_LIST = []

with open('Grantee_Ownership_Report_Links.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        URLS_LIST.append(row[0])
    URLS_LIST.pop(0)

CSV_FILE = 'pubmedia-board-members-data.csv'

CSV_HEADERS = [
    'Licensee',
    'City',
    'State',
    'Name',
    'Occupation',
    'Gender',
    'Ethnicity',
    'Race',
    'Voting Interest'
]

with open(CSV_FILE, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=CSV_HEADERS)
    writer.writeheader()
    for URL in URLS_LIST:
        r = requests.get(URL)

        sections = BeautifulSoup(r.text, 'html.parser').find_all('section')

        # Takes the licensee's name from the first table at the top of the page.
        licensee = sections[0].find_all('table')[0].find_all('td')[1].text.strip()

        # Translates the state abbreviations into their full names.
        state = state_fixes.get(sections[0].find_all('table')[1].find_all('td')[2].text.strip())
        city = sections[0].find_all('table')[1].find_all('td')[1].text.strip()

        # The 'tables' variable excludes the last table, which is a questionnaire about voting and equity interests.
        tables = sections[6].find_all('table')[:-1]

        for table in tables:
            tbody = table.find('tbody')
            row = tbody.find_all('tr')

            # The first (and sometimes second) table in the section is the licensee or its parent entity. By identifying
            # the type of table, the program skips tables for entities and only collects data on humans.
            if row[1].find_all('td')[0].text.strip() == 'Entity Name':
                # Checks for Tribal entities, which are excluded from our analysis.
                if row[11].find_all('td')[1].text.strip() == 'Interest holder is a Tribal nation or Tribal entity':
                    raise ValueError(f"Tribal entity found! Check {licensee}")
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
                'City': city,
                'State': state,
                'Name': name,
                'Occupation': occupation,
                'Gender': gender,
                'Ethnicity': ethnicity,
                'Race': race,
                'Voting Interest': voting
            })
