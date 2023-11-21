import requests
import bs4
url = "https://tavex.lv/valutu-kursi/"

saturs = requests.get(url)
lapas_saturs = bs4.BeatifulSoup(saturs.content, 'html.paraser')

table =lapas_saturs.find('table', class_ = 'list-table') #manualā meklēšana, inspektojot mājaslapu
# tr tags (rinda) ir daļa no tabulu, meklējam td tagu (kolonnu)
print(table)

# for row in table.tbody.find_all('tr'):
    