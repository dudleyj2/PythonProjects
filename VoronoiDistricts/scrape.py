import requests
import csv
from bs4 import BeautifulSoup
from string import ascii_uppercase


f = csv.writer(open('data/state-reps-db.csv', 'w', newline=''))

page = requests.get('https://www.britannica.com/topic/United-States-House-of-Representatives-Seats-by-State-1787120')
soup = BeautifulSoup(page.text, 'html.parser')

state_list = soup.find(class_='md-drag md-table-wrapper')
state_rows = state_list.find_all('tr')
print(type(state_rows))

for row in state_rows:
    state = row.contents[1].contents[0]
    reps = row.contents[3].contents[0]
    #print("State: " + state + " Reps: " + reps)
    f.writerow([state, reps])
