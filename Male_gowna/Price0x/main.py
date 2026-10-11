import cloudscraper
from bs4 import BeautifulSoup
import datetime
urls = {"media expert":"https://www.mediaexpert.pl/gaming/kierownice/kierownica-moza-racing-r5-pc?gad_source=1&gad_campaignid=20565452562&gclid=Cj0KCQjw2_TQBhCnARIsAF3-XhwTqOhhwDTAjwrnFYUV-tciiIAkH5JR3dOvj5IiaNjcgQlZkPpnk4waAvSgEALw_wcB"
, }
def get_time():
    return datetime.datetime.now().strftime("[%H:%M][%d:%m]")
def check_if_today_exists(file_content):
    today_date = datetime.datetime.now().strftime("[%d:%m]")
    return today_date in file_content
def get_price(shop_name,url,symbol,cl_):
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)
    print(response.status_code)
    soup = BeautifulSoup(response.text,"lxml")
    price = soup.find(symbol, class_=cl_)
    price = price.text
    price = price.replace("\u202f","")
    return f"{shop_name} - {price}zł"

with open("ceny_moza.txt", "a+", encoding="UTF-8") as file:
    file.seek(0)
    file_txt = file.read()
    if check_if_today_exists(file_txt):
        pass
    else:

        text = f'{get_price("media expert", urls["media expert"], "span", "whole")} - {get_time()}'
        file.write(text)
        file.write("\n")