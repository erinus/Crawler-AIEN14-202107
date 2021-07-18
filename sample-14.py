import requests
import pyquery

def GetNews(url):
    pass

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
    elm_div_flex_feature = doc('div.article-list-container div.flex-feature').items()

if __name__ == '__main__':
    GetNewsList()