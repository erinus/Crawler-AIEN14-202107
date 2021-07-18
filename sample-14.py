import time

import requests
import pyquery

def GetNews(url):
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
    elm_h1 = doc('div#article-header h1')
    title = elm_h1.text()
    elm_div_timestamp = doc('div#article-header div.timestamp')
    datetime = elm_div_timestamp.text()

    print(f'標題：{title}')
    print(f'時間：{datetime}')
    print('')

def GetNewsList():
    response = requests.get(
        url='https://tw.appledaily.com/realtime/new/',
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
    elms_div_flex_feature = doc('div.article-list-container div.flex-feature').items()

    elms_div_flex_feature = list(elms_div_flex_feature)
    print(len(elms_div_flex_feature))

    for elm_div_flex_feature in elms_div_flex_feature:
        # elm_span_headline = elm_div_flex_feature('div.storycard-headline > span.headline')
        # print(elm_span_headline.text())
        elm_a_url = elm_div_flex_feature('a')
        url = elm_a_url.attr('href')
        url = f'https://tw.appledaily.com{url}'
        GetNews(url)
        time.sleep(1)

if __name__ == '__main__':
    GetNewsList()