import bs4
import requests
import re
import urllib
from bs4 import BeautifulSoup
import ssl
import os

# 网页结构

# 首页：https://www.poliform.it/en-us/poliform
# 商品列表：https://www.poliform.it/en-us/products
# 商品详情：https://www.poliform.it/en-us/products/preview-2021/le-club

url_base = 'https://www.poliform.it/'
url_list = url_base + 'en-us/products'

debug = False

def saveProductInfo(item):
    directory = './'+item['name']
    isExists = os.path.exists(directory)
    if not isExists:
        os.makedirs(directory)

    # Save pictures?
    for i in range(0, len(item['pictures'])):
        pic_name = re.compile('https://www.poliform.it/ContentsFiles/(.*)').findall(item['pictures'][i])[0]
        filename = './'+item['name'] + '/' + pic_name
        # 请求https链接时需要添加
        ssl._create_default_https_context=ssl._create_unverified_context
        urllib.request.urlretrieve(item['pictures'][i], filename=filename)

    # Save names

    # Save designers

    # Save description

def getProductItem(link):
    # Get HTML of product items
    response = requests.get(url_base + link, timeout=30)
    html = response.content.decode("utf-8", "ignore")

    # todo: 相关的api不熟悉，改为xpath的方式会更简洁清晰， re应该有匹配一个的api替换掉findall
    item = {"name": re.compile('itemprop="name".*?>(.*?)</h1>').findall(html)[0],
            "pictures": re.compile('<div><img src="(.*?)".*?></div>').findall(html),
            # "designer": re.compile('<a href="/en-us/designers/.*?">(.*?)</a>').findall(html)[0],
            # "description": re.compile('itemprop="description".*?>(.*?)</p>').findall(html)[0]
            }

    saveProductInfo(item)

def getProductList():
    # Get HTML of all products
    response = requests.get(url_list, timeout=30)
    html = response.content.decode("utf-8", "ignore")

    # if debug, it will generate the html file of the website
    if(debug):
        fh = open('./product_list.html', 'w')
        fh.write(html)
        fh.close()

    product_link_pattern = '<a href="(.*?)" itemprop="url">'
    product_links = re.compile(product_link_pattern).findall(html)

    # for i in range(0, 1):
    print(len(product_links))
    for i in range(0, len(product_links)):
        getProductItem(product_links[i])

def main():
    getProductList()


main()
