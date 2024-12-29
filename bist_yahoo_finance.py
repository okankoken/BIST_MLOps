import yfinance as yf
import pandas as pd
import numpy as np
import time

# Hisse sembollerini içeren text dosyasının yolu
file_path = "bist_symbols_with_IS.txt"

# Dosyayı oku ve her satıra ".IS" ekle
with open(file_path, "r", encoding="utf-8") as file:
    bist_symbols = [line.strip() for line in file]

# Toplam hisse sembolü kontrolü
print(f"Toplam hisse: {len(bist_symbols)}")

# Sonuçları saklamak için boş bir liste
all_data = []

# Türkçe harfleri kaldıran yardımcı fonksiyon
def remove_turkish_chars(text):
    if isinstance(text, str):
        char_map = str.maketrans("çÇğĞıİöÖşŞüÜ", "cCgGiIoOsSuU")
        return text.translate(char_map)
    return text

# Her bir hisse için verileri çekme
for symbol in bist_symbols:
    for attempt in range(3):  # Maksimum 3 deneme
        try:
            print(f"Veri cekiliyor: {symbol}")
            time.sleep(2)  # İstekler arasında 2 saniye bekle

            # Hisse bilgilerini al
            ticker = yf.Ticker(symbol)
            info = ticker.info  # Hisse bilgileri

            # Kapsamlı geçmiş verilerini al (5 yıl)
            history = ticker.history(period="5y")

            # Performans hesaplamaları
            changes = {}
            for period in ["1mo", "3mo", "6mo", "1y", "3y", "5y"]:
                try:
                    hist_period = ticker.history(period=period)
                    changes[period] = (
                        (hist_period["Close"].iloc[-1] - hist_period["Close"].iloc[0])
                        / hist_period["Close"].iloc[0]
                        * 100
                    )
                except Exception:
                    changes[period] = None

            # Volatilite hesaplama
            log_returns = np.log(history['Close'] / history['Close'].shift(1))
            volatility = log_returns.std() * np.sqrt(252) if not log_returns.isnull().all() else None

            # İlgili bilgileri saklama
            all_data.append({
                "Hisse": remove_turkish_chars(symbol),
                "Adi": remove_turkish_chars(info.get("shortName", "")),
                "Sektor": remove_turkish_chars(info.get("sector", "")),
                "Alt Grup": remove_turkish_chars(info.get("industry", "")),
                "Aciklama": remove_turkish_chars(info.get("longBusinessSummary", "")),
                "Beta": info.get("beta", ""),
                "FiyatKazanc Orani": info.get("trailingPE", ""),
                "PDDD Orani": info.get("priceToBook", ""),
                "FiyatSatis Orani": info.get("priceToSalesTrailing12Months", ""),
                "Kar Marji (%)": info.get("profitMargins", "") * 100 if info.get("profitMargins") else "",
                "Dolasimdaki Lot": info.get("sharesOutstanding", ""),
                "Toplam Gelir": info.get("totalRevenue", ""),
                "Net Kar": info.get("netIncomeToCommon", ""),
                "Son Kapanis Fiyati": info.get("previousClose", ""),
                "52 Hafta En Yuksek": info.get("fiftyTwoWeekHigh", ""),
                "52 Hafta En Dusuk": info.get("fiftyTwoWeekLow", ""),
                "Ortalama Hacim (10 gun)": info.get("averageVolume10days", ""),
                "Temettu Verimi (%)": info.get("dividendYield", "") * 100 if info.get("dividendYield") else "",
                "Son Temettu Tarihi": info.get("dividendDate", ""),
                "Piyasa Degeri": info.get("marketCap", ""),
                "Son Fiyat": history["Close"].iloc[-1] if not history.empty else "",
                "1 Ay Degisim (%)": changes.get("1mo"),
                "3 Ay Degisim (%)": changes.get("3mo"),
                "6 Ay Degisim (%)": changes.get("6mo"),
                "1 Yil Degisim (%)": changes.get("1y"),
                "3 Yil Degisim (%)": changes.get("3y"),
                "5 Yil Degisim (%)": changes.get("5y"),
                "Volatilite": volatility
            })
            break  # Başarılı olursa döngüden çık
        except Exception as e:
            print(f"Veri alinirken hata olustu: {symbol} - {e}")
            if attempt == 2:  # 3. deneme de başarısızsa boş veri ekle
                all_data.append({
                    "Hisse": remove_turkish_chars(symbol),
                    "Adi": "",
                    "Sektor": "",
                    "Alt Grup": "",
                    "Aciklama": "",
                    "Beta": "",
                    "FiyatKazanc Orani": "",
                    "PDDD Orani": "",
                    "FiyatSatis Orani": "",
                    "Kar Marji (%)": "",
                    "Dolasimdaki Lot": "",
                    "Toplam Gelir": "",
                    "Net Kar": "",
                    "Son Kapanis Fiyati": "",
                    "52 Hafta En Yuksek": "",
                    "52 Hafta En Dusuk": "",
                    "Ortalama Hacim (10 gun)": "",
                    "Temettu Verimi (%)": "",
                    "Son Temettu Tarihi": "",
                    "Piyasa Degeri": "",
                    "Son Fiyat": "",
                    "1 Ay Degisim (%)": "",
                    "3 Ay Degisim (%)": "",
                    "6 Ay Degisim (%)": "",
                    "1 Yil Degisim (%)": "",
                    "3 Yil Degisim (%)": "",
                    "5 Yil Degisim (%)": "",
                    "Volatilite": ""
                })
            time.sleep(2)  # Başarısız denemeler arasında bekle

# Verileri bir DataFrame'e dönüştür
df = pd.DataFrame(all_data)

# Sonuçları CSV dosyasına kaydet
output_file = "bist_tum_hisseler_verileri.csv"
df.to_csv(output_file, index=False, encoding='utf-8')

print(f"Tum hisse verileri {output_file} dosyasina basariyla kaydedildi!")
