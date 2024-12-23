import yfinance as yf

# İndirmek istediğiniz hisse senedi sembolü (ör. "GARAN.IS" Garanti BBVA için)
ticker = "GARAN.IS"

# Hisse senedi verilerini indir
data = yf.download(ticker, start="2023-01-01", end="2023-12-31")

# Verileri kontrol et
print(data.head())

# Veriyi CSV dosyasına kaydet
data.to_csv(f"{ticker}_bist_data.csv", index=True)
