import re
import time

import requests
import pyquery

def GetBook(bid):
    response = requests.get(
        url=f'https://www.books.com.tw/products/{bid}',
        headers={
            'referer': f'https://www.books.com.tw/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    )
    if response.status_code != 200:
        print('not 200')
        return

    with open('book.html', 'wb') as f:
        f.write(response.content)

    doc = pyquery.PyQuery(response.text)
    elm_h1 = doc('div.container_24 h1')
    print(elm_h1.text())
    elm_strong = doc('div.container_24 ul.price li strong[class^="price"]')
    print(elm_strong.text())

def GetBooks(cid):
    response = requests.get(
        url=f'https://www.books.com.tw/web/{cid}/',
        headers={
            'referer': f'https://www.books.com.tw/web/{cid}/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    )
    if response.status_code != 200:
        print('not 200')
        return

    with open('books.html', 'wb') as f:
        f.write(response.content)

    doc = pyquery.PyQuery(response.text)
    elms_item = doc('div.wrap > div.item').items()
    for elm_item in elms_item:
        # print(elm_item)
        url = elm_item('a').attr('href')
        m = re.match(r'https://www.books.com.tw/products/(?P<bid>\d+)\?', url)
        bid = m.group('bid')
        GetBook(bid)
        print('')

if __name__ == '__main__':
    cid = 'books_nbtopm_19'
    GetBooks(cid)