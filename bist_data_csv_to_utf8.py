import pandas as pd

# Dosyayı doğru bir şekilde oku
df = pd.read_csv('bist_tum_hisseler_verileri.csv', encoding='utf-8')

# Tekrar kaydet, UTF-8 BOM ile
df.to_csv('bist_tum_hisseler_verileri_utf8.csv', index=False, encoding='utf-8-sig')
