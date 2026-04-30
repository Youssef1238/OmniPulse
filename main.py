from core.scraper import Scrape,Compare
import time
import random
import traceback
from ui.index import start

#url = input("Type the url: ")
#url = "https://www.goud.ma/topics/%d8%a7%d9%84%d8%b1%d8%a6%d9%8a%d8%b3%d9%8a%d8%a9/"
url = "https://www.bladi.net/maroc-sport.html"


try:
    """ while True:
        html_content = Scrape(url)

        Compare(url,html_content)
        time.sleep(60 + random.randint(-5,5)) """
    start()

except Exception as e:
    traceback.print_exc()