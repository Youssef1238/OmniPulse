from requests import *
from minifier import intelligent_minify
from win11toast import toast
import json
import time
import datetime
from ai import getSelectors

firstTime = True

#url = input("Type the url: ")
url = "https://www.goud.ma/topics/%d8%a7%d9%84%d8%b1%d8%a6%d9%8a%d8%b3%d9%8a%d8%a9/"

def Compare(target,id)->bool:
    with open('state.json','r') as f:
        data = json.load(f)
    for state in data["states"]:
        if state["target"] == target and state["last_seen"] != id:
            state["last_seen"] = id
            with open('state.json','w') as f:
                json.dump(data,f)
            return True
    return False

def Register(target,id):
    global firstTime
    firstTime = False
    with open('state.json','r') as f:
        data = json.load(f)
    for state in data["states"]:
        if state["target"] == target:
            return
    data["states"].append({"target":target,"last_seen":id})
    with open('state.json','w') as f:
                json.dump(data,f)






try:
    while True:
        response: Response = get(url)
        clean_html = intelligent_minify(response.text)
        #last_article = parser.select('.post')
        #last_article = parser.find_all('article')[1]
        #identifier = last_article['id']

        isChanged = False

        selectors = getSelectors(clean_html)
        print(selectors)

        """ if(firstTime):
            Register(url,identifier)
        else:
            isChanged = Compare(url,identifier)

        if(isChanged):
            print("A new Item Has BEEN ADDED !!!")
            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ------ {last_article.header.h1.a.text} -> {last_article.header.h1.a['href']}")
            toast("A new Item Has BEEN ADDED !!!",last_article.header.h1.a.text,on_click=last_article.header.h1.a['href'],duration="long")
        else:
            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ------  No changes") """
        time.sleep(10)

except Exception as e:
    print(f"Error Occured: {e}")