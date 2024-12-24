# BIST_MLOps

Bu proje, Borsa İstanbul'da (BIST) işlem gören hisse senetlerinin verilerini toplamayı ve analiz etmeyi amaçlamaktadır.

## Adımlar

1. **Hisse Sembol Dosyasını Oluşturma**
   - **`mynet_symbols_1.py`** çalıştırılarak **`bist_symbols.txt`** dosyası oluşturulur.

2. **Sembolleri Yahoo Finance Formatına Çevirme**
   - **`text.py`** çalıştırılarak **`bist_symbols_with_IS.txt`** dosyası oluşturulur.

3. **Tüm Hisselerin Verilerini Çekme**
   - **`bist_yahoo_finance.py`** çalıştırılarak (bu işlem biraz zaman alabilir) **`bist_tum_hisseler_verileri.csv`** veri seti oluşturulur.

---

Bu adımları takip ederek tüm BIST hisseleriyle ilgili verileri elde edebilirsiniz.
