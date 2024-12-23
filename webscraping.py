import requests
from bs4 import BeautifulSoup
import pandas as pd

# Veriyi çekmek için URL
url = "https://finans.mynet.com/borsa/hisseler/"

# HTTP isteği gönder
response = requests.get(url)

# Sayfanın içeriğini analiz et
soup = BeautifulSoup(response.text, 'html.parser')

# Tablo verilerini çek
table = soup.find('table', {'class': 'stock-table'})  # Tablo sınıfını kontrol et
rows = table.find_all('tr')[1:]  # İlk satır başlık olduğu için atlanır

data = []

for row in rows:
    cols = row.find_all('td')
    data.append([col.text.strip() for col in cols])

# Veriyi DataFrame'e dönüştür
columns = ['Hisse', 'Son Fiyat', 'Değişim', 'Kazanç', 'Hacim', 'Piyasa Değeri']  # Sütun adlarını kontrol et
df = pd.DataFrame(data, columns=columns)

# Veriyi kontrol et
print(df.head())

# Veriyi CSV'ye kaydet
df.to_csv('bist_data.csv', index=False)
