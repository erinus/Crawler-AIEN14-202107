import datetime
import time

import requests
import pyquery

def GetPost(url):
    print(url)
    response = requests.get(
        url=url,
        headers={
            'referer': f'https://www.google.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    )
    if response.status_code != 200:
        print('NOT 200')
        return

    with open('apple.html', 'wb') as f:
        f.write(response.content)

    doc = pyquery.PyQuery(response.text)



def GetPostList():
    response = requests.get(
        url='https://www.coolaler.com/reviews/',
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    )
    if response.status_code != 200:
        print('NOT 200')
        return

    with open('coolar.html', 'wb') as f:
        f.write(response.content)

    doc = pyquery.PyQuery(response.text)
    elms_div_porta_article_item = doc('div.porta-articles > div.porta-article-item').items()

    for elm_div_porta_article_item in elms_div_porta_article_item:
        elm_a = elm_div_porta_article_item('a.porta-article-header a')
        print(elm_a.text())


if __name__ == '__main__':
    GetPostList()