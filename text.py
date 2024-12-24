# Dosya yükleme ve işleme
input_file = "bist_symbols.txt"  # Yüklediğiniz dosyanın adı
output_file = "bist_symbols_with_IS.txt"  # Çıkış dosyası

# Hisse sembollerini işleme
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

# İşlenmiş semboller
processed_symbols = [line.split()[0] + ".IS\n" for line in lines]

# İşlenmiş sembolleri yazdırma ve kaydetme
with open(output_file, "w", encoding="utf-8") as file:
    file.writelines(processed_symbols)

print(f"Hisse sembollerine '.IS' eklenmiş hali '{output_file}' dosyasına kaydedildi!")
