from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Selenium için bir driver başlatın
driver = webdriver.Chrome()

# Yahoo Finance Lookup sayfasına gidin
driver.get("https://finance.yahoo.com/lookup")

# Arama kutusuna "IS" yaz ve Enter'a bas
search_box = driver.find_element(By.ID, "search-term")
search_box.send_keys("IS")
search_box.send_keys(Keys.RETURN)

time.sleep(5)  # Sayfanın yüklenmesini bekleyin

# Tüm hisse sembollerini bulun
symbols = driver.find_elements(By.CSS_SELECTOR, ".data-col0")

# Hisse sembollerini bir listeye kaydedin
bist_symbols = [symbol.text for symbol in symbols if ".IS" in symbol.text]

# Sonuçları yazdır
print(bist_symbols)

# Tarayıcıyı kapat
driver.quit()
