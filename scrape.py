from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(".\\chromedriver")
driver.get("https://www.walmart.ca/en/ip/nimbus9-cirrus-2-galaxy-a10e-black/6000200739606?rrid=richrelevance")

print(driver.page_source)
print("\nHTML content scraped")