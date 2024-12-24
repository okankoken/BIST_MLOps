import requests
from bs4 import BeautifulSoup

# Hisse senetlerinin listelendiği web sayfasının URL'si
url = 'https://finans.mynet.com/borsa/hisseler/'

# Sayfayı çek
response = requests.get(url)
if response.status_code != 200:
    raise Exception(f"Web sitesine ulaşılamıyor: {response.status_code}")

soup = BeautifulSoup(response.content, 'html.parser')

# Tüm tabloları kontrol et
tables = soup.find_all('table')
if not tables:
    raise Exception("Web sayfasında hiç tablo bulunamadı.")

# Hisse senetleri tablosunu bulmaya çalış
target_table = None
for table in tables:
    if "Hisse" in table.text:  # İçeriğe göre tabloyu bul
        target_table = table
        break

if not target_table:
    raise Exception("Hisse senetleri tablosu bulunamadı.")

# Hisse sembollerini bul
symbols = []
rows = target_table.find_all('tr')[1:]  # Başlık satırını atla
for row in rows:
    cols = row.find_all('td')
    if len(cols) > 0:
        symbol = cols[0].text.strip() + '.IS'  # Sembole '.IS' ekle
        symbols.append(symbol)

# Sonuçları kontrol et
print(symbols)

# Sembolleri bir dosyaya kaydet
with open('bist_symbols.txt', 'w') as f:
    for symbol in symbols:
        f.write(symbol + '\n')

print("Hisse sembolleri başarıyla kaydedildi: bist_symbols.txt")
