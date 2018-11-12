import requests
import csv
from bs4 import BeautifulSoup

# Collecting and parsing the first page
page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
soup = BeautifulSoup(page.text, 'html.parser')

# Remove bottom links
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

# Create a file to write the artists' names to
f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

# Pulling all text from the BodyText div
artist_names = soup.find(class_='BodyText')

# Pulling text from all instances of <a> tag within BodyText div
artist_name_items = artist_names.find_all('a')

# Create for loop to print out all artists' names
for artist_name in artist_name_items:
    names = artist_name.contents[0]
    links = 'http://web.archive.org' + artist_name.get('href')
    print(names)
    print(links)

    f.writerow([names,links])