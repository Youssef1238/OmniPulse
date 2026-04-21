from bs4 import BeautifulSoup

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