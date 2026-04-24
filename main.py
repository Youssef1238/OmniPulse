from requests import *
from utilities import intelligent_minify, get_deepest_text, get_full_link
from validator import validate_selectors
from win11toast import toast
import json
import time
import datetime
from ai import getSelectors
from bs4 import BeautifulSoup
import traceback
import random

firstTime = True

#url = input("Type the url: ")
#url = "https://www.goud.ma/topics/%d8%a7%d9%84%d8%b1%d8%a6%d9%8a%d8%b3%d9%8a%d8%a9/"
url = "https://www.bladi.net/maroc-sport.html"



def Notify(title,link):
    title = get_deepest_text(title)
    link = get_full_link(link,url)
    print("A new Item Has BEEN ADDED !!!")
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ------ {title} -> {link}")
    toast("A new Item Has BEEN ADDED !!!",title,on_click=link,duration="long")



def Compare(target,html_content):
    # load the data from the json
    with open('state.json','r') as f:
        data = json.load(f)

    # iterate the data to find the target
    for state in data["states"]:
        if state["target"] == target : 
            # if the target is found 
            bs_content = BeautifulSoup(html_content,'html.parser')
            clean_html = intelligent_minify(html_content)
            # validate selectors
            selectors = validate_selectors(clean_html,state["selectors"])
            # get the article
            article = bs_content.select_one(selectors["article"])
            link = article.select_one(selectors["link"])["href"]
            # update the last_seen if its different and save the data to the json file
            if state["last_seen"] != link:
                state["last_seen"] = link
                with open('state.json','w') as f:
                    json.dump(data,f)
                # Notify and return
                return Notify(article.select_one(selectors["title"]),article.select_one(selectors["link"])["href"])
                
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ------  No changes")

def Register(html_content,target):
    global firstTime
    # set firstTime to false to start comparing
    firstTime = False

    # load the data from the json file
    with open('state.json','r') as f:
        data = json.load(f)

    # if the target is already there , skip
    for state in data["states"]:
        if state["target"] == target:
            return
        
    # clean the html and get selectors
    clean_html = intelligent_minify(html_content)
    selectors = getSelectors(clean_html)
    # convert the selectors into a dict
    selectors = json.loads(selectors)

    # validate the selectors and re-prompt when needed
    selectors = validate_selectors(clean_html,selectors)

    # get the link
    content = BeautifulSoup(clean_html, 'html.parser')
    link = content.select_one(selectors["article"]).select_one(selectors["link"])["href"]

    # update the data and save to the file
    data["states"].append({"target":target,"last_seen":link,"selectors" : selectors})
    with open('state.json','w') as f:
                json.dump(data,f)






try:
    while True:
        response: Response = get(url,headers={"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"})
        html_content = response.text
        if(firstTime):
            Register(html_content,url)
        else:
            Compare(url,html_content)
        time.sleep(60 + random.randint(-5,5))

except Exception as e:
    traceback.print_exc()