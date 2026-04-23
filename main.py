from requests import *
from utilities import intelligent_minify, get_deepest_text, get_full_link
from win11toast import toast
import json
import time
import datetime
from ai import getSelectors
from bs4 import BeautifulSoup
import traceback

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
    with open('state.json','r') as f:
        data = json.load(f)
    for state in data["states"]:
        if state["target"] == target : 
            article = html_content.select_one(state["selectors"]["article"])
            link = article.select_one(state["selectors"]["link"])["href"]
            if state["last_seen"] != link:
                state["last_seen"] = link
                with open('state.json','w') as f:
                    json.dump(data,f)
                return Notify(article.select_one(state["selectors"]["title"]),article.select_one(state["selectors"]["link"])["href"])
                
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ------  No changes")

def Register(html_content,target):
    global firstTime
    firstTime = False
    with open('state.json','r') as f:
        data = json.load(f)

    for state in data["states"]:
        if state["target"] == target:
            return
    clean_html = intelligent_minify(html_content)
    selectors = getSelectors(clean_html)
    print(selectors)
    parser = BeautifulSoup(html_content, 'html.parser')
    selectors = json.loads(selectors)
    link = parser.select_one(selectors["article"]).select_one(selectors["link"])["href"]


    data["states"].append({"target":target,"last_seen":link,"selectors" : selectors})
    with open('state.json','w') as f:
                json.dump(data,f)






try:
    while True:
        response: Response = get(url)
        html_content = response.text
        if(firstTime):
            Register(html_content,url)
        else:
            Compare(url,BeautifulSoup(html_content,'html.parser'))
        time.sleep(10)

except Exception as e:
    traceback.print_exc()