import requests

url_main = 'https://www.poliform.it/'
url_product = 'https://www.poliform.it/en-us/products'
url_items = 'https://www.poliform.it/en-us/products/preview-2021/le-club'

def getHTMLText(url):
    data = {'idCategory' : 'new'}
    r = requests.post(url, data, timeout=30)
    print(r.content)
    return r.content

def main():
    url = 'https://www.cattelanitalia.com/en/products/productList/0/'
    getHTMLText(url)

main()
