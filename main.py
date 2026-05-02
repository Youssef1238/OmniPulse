from core.scraper import Scrape,Compare
import time
import random
import traceback
import webview
import os
from database.database import Database
from utils.helpers import get_full_link


class API:
    def __init__(self):
        self.db = Database()

    def route(self,path):
        window.load_url(path)

    def redirect(self,url):
        os.startfile(url)
    
    def get_link(self,url,path):
        return get_full_link(path,url)

    def load_data(self):
        data = self.db.findall()
        return data
    def log(self,content):
        print(content)


if __name__ == '__main__':
    api = API()
    window = webview.create_window('OmniPulse', url='ui/index.html',js_api=api)
    webview.start()







#url = input("Type the url: ")
#url = "https://www.goud.ma/topics/%d8%a7%d9%84%d8%b1%d8%a6%d9%8a%d8%b3%d9%8a%d8%a9/"
url = "https://www.bladi.net/maroc-sport.html"


""" try:
     while True:
        html_content = Scrape(url)

        Compare(url,html_content)
        time.sleep(60 + random.randint(-5,5)) 
    start()

except Exception as e:
    traceback.print_exc() """