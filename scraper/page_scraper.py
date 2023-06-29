import bs4
import requests

def get_text(url):
    response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = bs4.BeautifulSoup(response.text,'lxml')
    for string in soup.strings:
        print(repr(string))
    return soup.body.get_text(' ', strip=True)


