import yfinance as yf
import pandas as pd
import numpy as np

# Hisse sembollerini içeren text dosyasının yolu
file_path = "bist_symbols_with_IS.txt"

# Dosyayı oku ve her satıra ".IS" ekle
with open(file_path, "r") as file:
    bist_symbols = [line.strip() for line in file]

# Sonuçları kontrol et
print(bist_symbols)


# Sonuçları saklamak için boş bir liste
all_data = []

# Her bir hisse için verileri çekme
for symbol in bist_symbols:
    try:
        print(f"Veriler çekiliyor: {symbol}")

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
            except:
                changes[period] = None

        # Volatilite hesaplama
        log_returns = np.log(history['Close'] / history['Close'].shift(1))
        volatility = log_returns.std() * np.sqrt(252) if not log_returns.isnull().all() else None

        # İlgili bilgileri saklama
        all_data.append({
            "Hisse": symbol,
            "Adı": info.get("shortName", "Bilinmiyor"),
            "Sektör": info.get("sector", "Bilinmiyor"),  # Sektör bilgisi
            "Alt Grup": info.get("industry", "Bilinmiyor"),  # Alt grup bilgisi
            "Açıklama": info.get("longBusinessSummary", "Bilinmiyor"),  # Şirket açıklaması
            "Beta": info.get("beta", "Bilinmiyor"),
            "Fiyat/Kazanç Oranı": info.get("trailingPE", "Bilinmiyor"),
            "PD/DD Oranı": info.get("priceToBook", "Bilinmiyor"),
            "Fiyat/Satış Oranı": info.get("priceToSalesTrailing12Months", "Bilinmiyor"),
            "Kâr Marjı (%)": info.get("profitMargins", "Bilinmiyor") * 100 if info.get("profitMargins") else None,
            "Dolaşımdaki Lot": info.get("sharesOutstanding", "Bilinmiyor"),
            "Toplam Gelir": info.get("totalRevenue", "Bilinmiyor"),
            "Net Kâr": info.get("netIncomeToCommon", "Bilinmiyor"),
            "Son Kapanış Fiyatı": info.get("previousClose", "Bilinmiyor"),
            "52 Hafta En Yüksek": info.get("fiftyTwoWeekHigh", "Bilinmiyor"),
            "52 Hafta En Düşük": info.get("fiftyTwoWeekLow", "Bilinmiyor"),
            "Ortalama Hacim (10 gün)": info.get("averageVolume10days", "Bilinmiyor"),
            "Temettü Verimi (%)": info.get("dividendYield", "Bilinmiyor") * 100 if info.get("dividendYield") else None,
            "Son Temettü Tarihi": info.get("dividendDate", "Bilinmiyor"),
            "Piyasa Değeri": info.get("marketCap", "Bilinmiyor"),
            "Son Fiyat": history["Close"].iloc[-1] if not history.empty else None,
            "1 Ay Değişim (%)": changes.get("1mo"),
            "3 Ay Değişim (%)": changes.get("3mo"),
            "6 Ay Değişim (%)": changes.get("6mo"),
            "1 Yıl Değişim (%)": changes.get("1y"),
            "3 Yıl Değişim (%)": changes.get("3y"),
            "5 Yıl Değişim (%)": changes.get("5y"),
            "Volatilite": volatility
        })
    except Exception as e:
        print(f"Veriler alınırken hata oluştu: {symbol} - {e}")

# Verileri bir DataFrame'e dönüştür
df = pd.DataFrame(all_data)

# Sonuçları CSV dosyasına kaydet
df.to_csv("bist_tum_hisseler_verileri.csv", index=False)

print("Tüm BIST hisseleri başarıyla bist_tum_hisseler_verileri.csv dosyasına kaydedildi!")
