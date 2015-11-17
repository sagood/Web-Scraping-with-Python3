from urllib.request import urlopen
from urllib.parse import unquote
from bs4 import BeautifulSoup
import datetime
import random
import re


random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
    #html = urlopen("http://zh.wikipedia.org/wiki/%E5%87%AF%E6%96%87%C2%B7%E8%B4%9D%E8%82%AF")
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks("/wiki/Keven_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(unquote(newArticle))
    links = getLinks(newArticle)
