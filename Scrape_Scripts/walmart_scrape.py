from selenium import webdriver
from bs4 import BeautifulSoup


def scrape_walmart(pro_name, pro_id):
    driver = webdriver.Chrome("..\\chromedriver")
    driver.get("https://www.walmart.ca/en")
    try:
        searchbox_input = driver.find_elements_by_tag_name("input")[0]
        searchbox_input.send_keys(pro_name)
        searchbox_input.submit()

        search_menu = BeautifulSoup(driver.page_source, features="html.parser")
        product_links = search_menu.findAll(
            "a", attrs={
                "class": "product-link",
                'href': True
            })

        for i in range(5):
            driver.get("https://www.walmart.ca" + product_links[i]["href"])
            soup = BeautifulSoup(driver.page_source, features="html.parser")

            # Scrape time
            price = soup.find(
                'span', attrs={
                    "data-automation": "buybox-price"
                }).contents[0]

            product_id = soup.findAll(
                "div", attrs={
                    "class": "e1cuz6d13",
                    "class": "css-1yyoz8v"
                })
            model_no = product_id[-3].contents[0]

            if model_no == pro_id:
                return price[1:]
    except Exception:
        pass
    finally:
        driver.close()

    return 'Undefined'
