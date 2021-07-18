import datetime
import time
import re

import requests
import pyquery

def GetPost(url):
    print(url)
    response = requests.get(
        url=url,
        headers={
            'referer': f'https://www.coolaler.com/reviews/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    )
    if response.status_code != 200:
        print('NOT 200')
        return

    with open('coolar.html', 'wb') as f:
        f.write(response.content)

    doc = pyquery.PyQuery(response.text)

    title = doc('div.p-title').text()

    date = doc('div.p-description time').attr('datetime')
    date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z')
    date = date.strftime('%Y-%m-%d %H:%M:%S')

    content = doc('div.bbWrapper').text()
    content = re.sub(r'\n+', '\n', content)

    print(f'標題：{title}')
    print(f'時間：{date}')
    print(f'內文：')
    print(content)
    print('')

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
        url = elm_a.attr('href')
        url = f'https://www.coolaler.com{url}'
        GetPost(url)
        time.sleep(1)

if __name__ == '__main__':
    GetPostList()