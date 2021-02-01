import bs4
import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status() # generate error information
        r.encoding = r.apparent_encoding # could be revised to enhance the speed
        return r.content # return the HTML to other parts of the programmme
    except:
        return ""

def fillUnivKust(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for a in soup.find('li').children:
        if isinstance(a, bs4.element.Tag): # avoid String type's data
            aaa = a('div') # There are only 2 divs here in this case
            ulist.append([aaa[0].string]) # aaa[0] -> Product's name

def printUnivList(ulist, num):
    for i in range(num):
        u = ulist[i] # u already have
        print(u[i]) # print the ith product's name

def main():
    uinfo = []
    url = 'https://www.cattelanitalia.com/en/products?c=new'
    html = getHTMLText(url)
    fillUnivKust(uinfo, html)
    printUnivList(uinfo, 25)

main()
