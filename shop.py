import requests
from bs4 import BeautifulSoup
from threading import Timer
import telebot

API_TOKEN = '1911292558:AAGWCfwlhNoFX9t2_mRSyfW_aG-PvGIlDBU'
shop_url = 'https://fortnitetracker.com/shop'
# bot = telebot.TeleBot(API_TOKEN)

def get_shop_items():
    page_shop = requests.get(shop_url)
    shop_soup = BeautifulSoup(page_shop.text,'html.parser')
    all_items = shop_soup.findAll('a', class_='fortnite-db-item')
    print(all_items)

print(get_shop_items())
# bot.polling(none_stop=True)


# h350yam 2021
