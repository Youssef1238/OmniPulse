from requests import *
from bs4 import BeautifulSoup




url = input("Type the url: ")

try:
    response: Response = get(url)
    parser = BeautifulSoup(response.text, 'html.parser')
    print(parser.p.string)

except Exception as e:
    print(f"Error Occured: {e}")