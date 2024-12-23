from selenium import webdriver

# Start a browser session
driver = webdriver.Chrome()  # Ensure ChromeDriver is in your PATH or same directory
driver.get("https://www.google.com")

# Close the browser
driver.quit()
