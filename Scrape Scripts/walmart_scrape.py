from selenium import webdriver
from bs4 import BeautifulSoup
import json

driver = webdriver.Chrome(".\\chromedriver")
driver.get("https://www.walmart.ca/en")

searchbox_input = driver.find_elements_by_tag_name("input")[0]
searchbox_input.send_keys(
    "HP Stream 14\" Laptop 4GB 32GB Windows 10 Violet Purple Bluetooth Windows 10"
)
searchbox_input.submit()

search_menu = BeautifulSoup(driver.page_source, features="html.parser")
product_links = search_menu.findAll(
    "a", attrs={
        "class": "product-link",
        'href': True
    })

item_dict = {}
for i in range(5):
    driver.get("https://www.walmart.ca" + product_links[i]["href"])
    soup = BeautifulSoup(driver.page_source, features="html.parser")
    item_dict[i] = {}

    # Scrape time
    item_dict[i]['name'] = soup.find(
        'h1', attrs={
            "data-automation": "product-title"
        }).contents[0]
    item_dict[i]['price'] = soup.find(
        'span', attrs={
            "data-automation": "buybox-price"
        }).contents[0]

    product_id = soup.findAll(
        "div", attrs={
            "class": "e1cuz6d13",
            "class": "css-1yyoz8v"
        })
    item_dict[i]["Model #"] = product_id[-3].contents[0]
    item_dict[i]["SKU"] = product_id[-2].contents[0]
    item_dict[i]["UPC"] = product_id[-1].contents[0]

driver.close()

with open("walmart_data.json", "w", encoding="utf-8") as json_outfile:
    json.dump(item_dict, json_outfile)
