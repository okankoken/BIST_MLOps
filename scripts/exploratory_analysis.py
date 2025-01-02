import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veri setini yükleme
file_path = r"D:\VBO_MLOps_Bootcamp_4\BIST_MLOps\bist_tum_hisseler_verileri.csv"
df = pd.read_csv(file_path)

df.shape
df.head(10)
df.info
df.dtypes
df.columns
df.describe().T
df.isnull().sum()


# Genel Bilgiler
print("Veri Setinin İlk 5 Satırı:")
print(df.head())
print("\nVeri Setinin Boyutları:", df.shape)
print("\nSütun İsimleri:", df.columns.tolist())
print("\nVeri Setinin Genel Bilgisi:")
print(df.info())

# Eksik Değer Analizi
missing_values = df.isnull().sum()
missing_percentage = (missing_values / len(df)) * 100
print("\nEksik Değerler ve Yüzdeleri:")
print(pd.DataFrame({"Eksik Değer Sayısı": missing_values, "Yüzde (%)": missing_percentage}))

# Temel İstatistikler
print("\nTemel İstatistikler:")
print(df.describe(include='all'))

# Sektörel Dağılım
sector_counts = df['Sektor'].value_counts()
print("\nSektörel Dağılım:")
print(sector_counts)

# Sektörel Dağılımın Görselleştirilmesi
plt.figure(figsize=(10, 6))
sector_counts.plot(kind='bar', color='skyblue')
plt.title("Sektörel Dağılım")
plt.xlabel("Sektör")
plt.ylabel("Hisse Sayısı")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Fiyat İstatistikleri
plt.figure(figsize=(10, 6))
sns.histplot(df['Son Kapanis Fiyati'].dropna(), bins=30, kde=True, color='purple')
plt.title("Son Kapanış Fiyatı Dağılımı")
plt.xlabel("Son Kapanış Fiyatı")
plt.ylabel("Frekans")
plt.tight_layout()
plt.show()

# Getiri Oranları (3 Ay, 6 Ay ve 1 Yıl)
for column in ['3 Ay Degisim (%)', '6 Ay Degisim (%)', '1 Yil Degisim (%)']:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df[column].dropna(), color='orange')
    plt.title(f"{column} Dağılımı")
    plt.xlabel(column)
    plt.tight_layout()
    plt.show()

# Beta Değerlerinin Dağılımı
plt.figure(figsize=(10, 6))
sns.histplot(df['Beta'].dropna(), bins=30, kde=True, color='green')
plt.title("Beta Değerlerinin Dağılımı")
plt.xlabel("Beta")
plt.ylabel("Frekans")
plt.tight_layout()
plt.show()

# Temettü Verimi Dağılımı
plt.figure(figsize=(10, 6))
sns.histplot(df['Temettu Verimi (%)'].dropna(), bins=30, kde=True, color='blue')
plt.title("Temettü Verimi Dağılımı")
plt.xlabel("Temettü Verimi (%)")
plt.ylabel("Frekans")
plt.tight_layout()
plt.show()

# Sadece sayısal sütunları seç
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Korelasyon matrisi
correlation_matrix = df[numerical_columns].corr()

# Korelasyon matrisini görselleştir
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', cbar=True)
plt.title("Finansal Metrikler Korelasyon Matrisi")
plt.tight_layout()
plt.show()

print("Keşifçi Veri Analizi tamamlandı.")
