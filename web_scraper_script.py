from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time



# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in your PATH or same directory
url = "https://finans.mynet.com/borsa/hisseler/"
driver.get(url)
time.sleep(5)  # Wait for 5 seconds


# Get the page source and parse it
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the table with stock data
table = soup.find('table', {'class': 'stock-table'})

if table:
    rows = table.find_all('tr')[1:]  # Skip the header row
    data = []
    for row in rows:
        cols = row.find_all('td')
        data.append([col.text.strip() for col in cols])

    # Create a DataFrame
    columns = ['Hisse', 'Son Fiyat', 'Değişim', 'Kazanç', 'Hacim', 'Piyasa Değeri']
    df = pd.DataFrame(data, columns=columns)

    # Print and save the data
    print(df.head())
    df.to_csv('bist_data.csv', index=False)
else:
    print("Table not found. Verify the class name or the page structure.")

# Close the browser
driver.quit()
