import requests
import csv
from bs4 import BeautifulSoup
from string import ascii_uppercase


f = csv.writer(open('artist-db.csv', 'w'))
f.writerow(['Name', 'Nationality', 'Years', 'Link'])

pages = []

for c in ascii_uppercase:
    i = 1
    http_status = True
    while(http_status):
        url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/an' + c + str(i) + '.htm'
        current_page = requests.get(url)

        print(str(c) + " " + str(i))

        # continue if we get a 200 response code
        if current_page.status_code is 200:
            pages.append(url)
        else:
            http_status = False
        i += 1



for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    artist_list = soup.find(class_='BodyText')
    artist_info = artist_list.find_all('td')

    index = 0
    while index < len(artist_info)-2:
        name = artist_info[index].string

        nation = ""
        years = ""
        nation_and_years_str = str(artist_info[index+1].string)
        if nation_and_years_str == "None":
            nation = "NA"
            years = "NA"
        elif nation_and_years_str != "":
            if ',' in nation_and_years_str:
                nation_and_years = [x.strip() for x in nation_and_years_str.split(',')]
                nation = nation_and_years[0]
                years = nation_and_years[1]
            elif '1' in nation_and_years_str:
                years = nation_and_years_str
            else:
                nation = nation_and_years_str
        
        artist_link = artist_info[index].find('a')
        link = 'https://web.archive.org' + artist_link.get('href')
        
        f.writerow([name, nation, years, link])
        index += 2
