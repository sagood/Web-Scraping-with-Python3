from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj = BeautifulSoup(html, 'html.parser')
content = bsObj.find('div', {'id': 'mw-content-text'}).get_text()
content = bytes(content, 'utf-8')
content = content.decode('utf-8')
print(content)
