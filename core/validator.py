from bs4 import BeautifulSoup
from ai import getSelectors

def validate_selectors(content,selectors):
    content_bs = BeautifulSoup(content,"html.parser")
    new_selectors = selectors

    if(content_bs.select_one(selectors["article"]) == None):
        new_selectors = getSelectors(content,f"\nNote: you already have given me the selector of article as : {selectors['article']} but its wrong , there is no such selector.")
        return validate_selectors(content,new_selectors)
    
    if(content_bs.select_one(selectors["link"]) == None):
        new_selectors = getSelectors(content,f"\nNote: you already have given me the selector of link as : {selectors['link']} but its wrong , there is no such selector.")
        return validate_selectors(content,new_selectors)
    
    if(content_bs.select_one(selectors["link"])["href"] == None):
        new_selectors = getSelectors(content,f"\nNote: you already have given me the selector of link as : {selectors['link']} but its wrong , the element has no href attribute.")
        return validate_selectors(content,new_selectors)
    
    if(content_bs.select_one(selectors["title"]) == None):
        new_selectors = getSelectors(content,f"\nNote: you already have given me the selector of link as : {selectors['title']} but its wrong , there is no such selector.")
        return validate_selectors(content,new_selectors)
    
    return new_selectors




