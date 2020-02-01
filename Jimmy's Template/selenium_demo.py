from selenium import webdriver

driver = webdriver.Chrome(".\\chromedriver")

driver.get("https://www.bcit.ca/hr/contacts/")

print(driver.page_source)

print("\nHTML content scraped")