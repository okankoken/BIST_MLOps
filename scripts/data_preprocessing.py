import pandas as pd
import numpy as np

# Veri setini oku
input_file = (r"D:\VBO_MLOps_Bootcamp_4\BIST_MLOps\bist_tum_hisseler_verileri.csv")
df = pd.read_csv(input_file, encoding="utf-8")

df.isnull().sum()

# Kategorik ve sayısal sütunları ayır
categorical_columns = ["Hisse", "Adi", "Sektor", "Alt Grup", "Aciklama"]
all_columns = set(df.columns)
numerical_columns = list(all_columns - set(categorical_columns))  # Sayısal sütunları belirle

# Mevcut sütunlarla kontrol yap
numerical_columns = [col for col in numerical_columns if col in df.columns]

# 1. inf ve -inf değerlerini tespit et ve doldur
for col in numerical_columns:
    if col in df.columns:
        # inf değerlerini sütun bazlı maksimum ile değiştir
        max_val = df[df[col] != np.inf][col].max()
        df[col] = df[col].replace(np.inf, max_val)

        # -inf değerlerini sütun bazlı minimum ile değiştir
        min_val = df[df[col] != -np.inf][col].min()
        df[col] = df[col].replace(-np.inf, min_val)

# 2. Eksik veri oranı %50'den fazla olan sütunları kaldır
threshold = len(df) * 0.5
df = df.dropna(axis=1, thresh=threshold)

# 3. Kategorik sütunlardaki eksik değerleri "N/A" ile doldur
for col in categorical_columns:
    if col in df.columns:
        df[col] = df[col].fillna("N/A")

# 4. Sayısal sütunlardaki eksik değerleri sektör bazlı veya genel ortalama ile doldur
if "Sektor" in df.columns:
    for col in numerical_columns:
        if col in df.columns:
            # Sektör bazlı ortalama ile doldurma
            df[col] = df.groupby("Sektor")[col].transform(
                lambda x: x.fillna(x.mean())
            )

# Eğer hala eksik değer varsa genel ortalama ile doldurma
numerical_columns = [col for col in numerical_columns if col in df.columns]
df[numerical_columns] = df[numerical_columns].fillna(df[numerical_columns].mean())

# Temizlenmiş veri setini kaydet
output_file = "D:\VBO_MLOps_Bootcamp_4\BIST_MLOps\data/bist_tum_hisseler_temizlenmis.csv"
df.to_csv(output_file, index=False, encoding="utf-8")

print(f"Temizlenmiş veri seti {output_file} dosyasına başarıyla kaydedildi!")