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

CSV_FILE = 'dates.csv'

CSV_HEADERS = ['Date']

with open(CSV_FILE, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=CSV_HEADERS)
    writer.writeheader()
    for URL in URLS_LIST:
        r = requests.get(URL)

        src = BeautifulSoup(r.text, 'html.parser').find_all('dl')

        # Takes the licensee's name from the first table at the top of the page.
        date = src[0].find_all('dd')[1].text.strip()

        # Write the row
        writer.writerow({'Date': date,})
