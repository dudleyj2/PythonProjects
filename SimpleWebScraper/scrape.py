import requests
import csv
from bs4 import BeautifulSoup
from string import ascii_uppercase


f = csv.writer(open('artist-names.csv', 'w'))
f.writerow(['Name', 'Nationality', 'Link'])

pages = ['https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm']

#for c in ascii_uppercase:
#    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/an' + c + '1.htm'
#    pages.append(url)


for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    artist_name_list = soup.find(class_='BodyText')
    artist_info = artist_name_list.find_all('td')

    print("1:  " + str(artist_info[0]))
    print("2:  " + str(artist_info[1]))
    print("3:  " + str(artist_info[2]))
    print("4:  " + str(artist_info[3]))
    print("5:  " + str(artist_info[4]))
    print("6:  " + str(artist_info[5]))


    index = 0
    while index < len(artist_info):
        name = artist_info[index+1]
        nationality = artist_info[index+2]
        link = 'https"//web.archive.org' + artist_info[index].get('href')
        f.writerow([name, nationality, link])
        index += 3
