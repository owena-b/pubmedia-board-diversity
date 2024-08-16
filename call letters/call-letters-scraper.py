import requests
import csv
from bs4 import BeautifulSoup
from fixes import state_fixes

URLS_LIST = []

with open('../source data scrape/Grantee_Ownership_Report_Links.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        URLS_LIST.append(row[0])
    URLS_LIST.pop(0)

CSV_FILE = 'call-letters.csv'

CSV_HEADERS = [
    'Licensee',
    'City',
    'State',
    'Callsigns'
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
        table = sections[4].find_all('table')[1].find('tbody')

        callsigns = []

        for row in table.find_all('tr'):
            lines = row.find_all('td')
            callsigns.append(lines[1].text.strip())

        callsigns = str(callsigns)[1:-1].replace("'", "")

        # Write the row
        writer.writerow({
            'Licensee': licensee,
            'City': city,
            'State': state,
            'Callsigns': callsigns
        })
