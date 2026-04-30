from requests import *
from utils.helpers import intelligent_minify, get_deepest_text, get_full_link
from utils.validator import validate_selectors
from database.database import Database
from win11toast import toast
import json
import datetime
from core.ai import getSelectors
from bs4 import BeautifulSoup
import random




db = Database()

def Notify(url,title,link):
    link = get_full_link(link,url)
    print("A new Item Has BEEN ADDED !!!")
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ------ {title} -> {link}")
    toast("A new Item Has BEEN ADDED !!!",title,on_click=link,duration="long")

def Compare(url,html_content):
    bs_content = BeautifulSoup(html_content,'html.parser')
    clean_html = intelligent_minify(html_content)
    target = db.find_target_by_url(url)

    if target is not None:
        
        # validate selectors
        selectors = validate_selectors(clean_html,target["selectors"])
        selectors_dict = json.loads(selectors)
        # get the article
        article = bs_content.select_one(selectors_dict["article"])
        link = article.select_one(selectors_dict["link"])["href"]
        title = article.select_one(selectors_dict["title"])
        title = get_deepest_text(title)
        last_seen = target["last_seen"]
        if last_seen != link:
            db.update_state(target["id"],link,title)
            # Notify and return
            return Notify(url,title,link)
        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ------  No changes")
    else:
        selectors = getSelectors(clean_html)
        # validate the selectors and re-prompt when needed
        selectors = validate_selectors(clean_html,selectors)

        # convert the selectors into a dict
        selectors_dict = json.loads(selectors)
        article = bs_content.select_one(selectors_dict["article"])
        link = article.select_one(selectors_dict["link"])["href"]
        title = article.select_one(selectors_dict["title"])
        title = get_deepest_text(title)

        db.create_target(url,"something"+str(random.randint(1,1000)),link,title,selectors) 


    
                
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ------  No changes")


def Scrape(url):
    response: Response = get(url,headers={"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"})
    return response.text



