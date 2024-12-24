import requests
from bs4 import BeautifulSoup

# Hisse senetlerinin listelendiği web sayfasının URL'si
url = 'https://finans.mynet.com/borsa/hisseler/'

# Sayfayı çek
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Hisse sembollerini bul
symbols = []
for row in soup.find_all('tr'):
    cols = row.find_all('td')
    if len(cols) > 0:
        symbol = cols[0].text.strip() + '.IS'
        symbols.append(symbol)

# Sonuçları kontrol et
print(symbols)