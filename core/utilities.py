from bs4 import BeautifulSoup
from urllib import parse


def get_full_link(link,url):
    if not link:
        return None
    
    return parse.urljoin(url,link)
    

def get_deepest_text(element):
    """
    Recursively finds the deepest child node that contains text.
    Prevents grabbing 'noise' from parent containers.
    """
    # If the element has no children, return its text
    if not list(element.children):
        return element.get_text(strip=True)
    
    # Check children. 
    for child in element.children:
        # If the child is a just text, return it
        if isinstance(child, str) and child.strip():
            return child.strip()
        # If it's a tag, dive deeper
        if child.name:
            res = get_deepest_text(child)
            if res:
                return res
                
    return element.get_text(strip=True)


def intelligent_minify(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # 1. Destroy useless tags entirely
    for tag in soup(['script', 'style', 'nav', 'footer', 'svg', 'path', 'img', 'iframe', 'noscript', 'aside','p','li']):
        tag.decompose()

    # 2. Iterate through every remaining tag on the page
    allowed_attrs = ['class', 'id', 'href']
    for tag in soup.find_all(True):
        
        # A. Strip useless attributes (keep only class, id, href)
        attrs = dict(tag.attrs)
        for attr in attrs:
            if attr not in allowed_attrs:
                del tag[attr]
                
        # B. Truncate long inner text to save tokens
        if tag.string:
            tag.string = ""

    # 3. Extract the body (now a lightweight skeleton)
    body = soup.find('body')
    if not body:
        return ""

    # Return the FULL body, no slicing needed!
    return str(body)