from requests import *
from bs4 import BeautifulSoup
import json
import time
import datetime

firstTime = True

#url = input("Type the url: ")
url = "https://fitgirl-repacks.site/"

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
        parser = BeautifulSoup(response.text, 'html.parser')
        last_article = parser.find_all('article')[1]
        identifier = last_article['id']

        isChanged = False

        if(firstTime):
            Register(url,identifier)
        else:
            isChanged = Compare(url,identifier)

        if(isChanged):
            print("A new Item Has BEEN ADDED !!!")
            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ------ {last_article.header.h1.a.text} -> {last_article.header.h1.a['href']}")
        else:
            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ------  No changes")
        time.sleep(60)

except Exception as e:
    print(f"Error Occured: {e}")