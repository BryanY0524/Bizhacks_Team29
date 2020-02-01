# from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import json

CONTACT_PAGE_URL = "https://www.bcit.ca/hr/contacts/"
EVENTBRITE_URL = "https://www.eventbrite.ca/o/isaca-vancouver-17805490026"


def get_HTML(url):
    '''Uses requests to grab HTML content from URL'''
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        'Content-Type':
        'text/html',
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(response.status_code)
    else:
        if url == CONTACT_PAGE_URL:
            parse_content_contact(response.content)
        else:
            parse_content_eventbrite(response.content)


def parse_content_contact(content):
    '''Parses content from HTML content'''
    id_counter = 1
    td_dict = {id_counter: {"part1": "", "phone #": ""}}

    soup = BeautifulSoup(content, features="html.parser")
    primary_div = soup.find('div', attrs={"id": "t_primary"})
    all_td = primary_div.findAll('td')  # Array of table cells

    for index, td in enumerate(all_td):
        if index > 1 and index % 2 == 0:
            id_counter += 1
            td_dict[id_counter] = {}

        if index % 2 == 0 or index == 0:  # if odd
            td_dict[id_counter]["part1"] = str(td)
        else:
            td_dict[id_counter]['phone #'] = str(td)

    try:
        with open("data.json", "w", encoding="utf-8") as json_outfile:
            json.dump(td_dict, json_outfile)

        with open("data.txt", "w", encoding="utf-8") as txt_outfile:
            for td in all_td:
                txt_outfile.write(str(td))
    except Exception as e:
        print(e)


def parse_content_eventbrite(content):
    '''Parses content from HTML content'''
    div_dict = {}

    soup = BeautifulSoup(content, features="html.parser")
    primary_div = soup.find('article', attrs={"id": "live_events"})
    div1 = primary_div.findAll('div', attrs={
                              "class": "list-card-v2 l-mar-top-2 js-d-poster"})  # Array of table cells

    for index, value in enumerate(div1):
        div_dict[index] = {}
        div_dict[index]["Title"] = value['data-share-name']
        div_dict[index]["Admission Fee"] = value.find('span').contents[0]
        div_dict[index]["Venue"] = (value.find('time')).contents[0][41:]

    try:
        with open("data1.json", "w", encoding="utf-8") as json_outfile:
            json.dump(div_dict, json_outfile)

        # with open("data1.txt", "w", encoding="utf-8") as txt_outfile:
        #     for event in div:
        #         txt_outfile.write(str(event))
    except Exception as e:
        print(e)


# driver = webdriver.Chrome(
#     "C:\\Users\\Jimmy\\Desktop\\Web Scraping Examples\\Python\\chromedriver")

# driver.get("https://www.bcit.ca/hr/contacts/")

if __name__ == "__main__":
    user_input=input("Enter 1 for contact page demo, any for Eventbrite: ")
    if user_input == "1":
        url=CONTACT_PAGE_URL
    else:
        url=EVENTBRITE_URL
    get_HTML(url)
    input("Files successfully created")
