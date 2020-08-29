import requests
from bs4 import BeautifulSoup

url = "https://weather.com/es-CO/tiempo/hoy/l/c1cdc854c06b7fe145827400f82eb319c2bb41e956f8ac0b52ab94180aed77c4"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('span', datatestid="TemperatureValue") #get tittle of time
for result in results:
    print(result.text)