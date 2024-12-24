import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# CSV dosyasını oku
file_path = "bist_tum_hisseler_verileri.csv"
df = pd.read_csv(file_path)

# Veriyi kontrol et
print("İlk 5 Satır:")
print(df.head(50))

# Eksik değerleri kontrol et
missing_values = df.isnull().sum()
print("\nEksik Değerler:")
print(missing_values)

# Temel istatistikler
print("\nTemel İstatistikler:")
print(df.describe())

# En yüksek piyasa değerine sahip 10 hisse
top_market_cap = df.nlargest(10, "Piyasa Değeri")
print("\nEn Yüksek Piyasa Değerine Sahip 10 Hisse:")
print(top_market_cap[["Hisse", "Piyasa Değeri"]])

# Fiyat/Kazanç oranına göre sıralama
top_pe_ratio = df.nlargest(10, "Fiyat/Kazanç Oranı")
print("\nEn Yüksek Fiyat/Kazanç Oranına Sahip 10 Hisse:")
print(top_pe_ratio[["Hisse", "Fiyat/Kazanç Oranı"]])

# 1 yıllık değişime göre en yüksek artış gösteren hisseler
top_1y_change = df.nlargest(10, "1 Yıl Değişim (%)")
print("\n1 Yıllık En Yüksek Artış Gösteren 10 Hisse:")
print(top_1y_change[["Hisse", "1 Yıl Değişim (%)"]])

# Görselleştirme
plt.figure(figsize=(10, 6))
plt.bar(top_market_cap["Hisse"], top_market_cap["Piyasa Değeri"])
plt.title("En Yüksek Piyasa Değerine Sahip 10 Hisse")
plt.xlabel("Hisse")
plt.ylabel("Piyasa Değeri (TRY)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_market_cap.png")  # Görseli kaydet
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(top_pe_ratio["Hisse"], top_pe_ratio["Fiyat/Kazanç Oranı"])
plt.title("En Yüksek Fiyat/Kazanç Oranına Sahip 10 Hisse")
plt.xlabel("Hisse")
plt.ylabel("Fiyat/Kazanç Oranı")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_pe_ratio.png")  # Görseli kaydet
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(top_1y_change["Hisse"], top_1y_change["1 Yıl Değişim (%)"])
plt.title("1 Yıllık En Yüksek Artış Gösteren 10 Hisse")
plt.xlabel("Hisse")
plt.ylabel("Değişim (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_1y_change.png")  # Görseli kaydet
plt.show()
