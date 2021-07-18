import urllib.parse

import requests
import pyquery

cookie = '<請輸入自己的 Cookie>'

def CheckStatus():
    global cookie
    response = requests.get(
        url='https://shopee.tw/api/v2/user/account_info?from_wallet=false&skip_address=1&need_cart=1',
        headers={
            'cookie': cookie,
            'referer': 'https://shopee.tw/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'x-api-source': 'pc',
            'x-csrftoken': 'NCaZXYtwXQOI7pth3q74h4msPjfYcsd6',
            'x-requested-with': 'XMLHttpRequest',
            'x-shopee-language': 'zh-Hant'
        }
    )
    if response.status_code != 200:
        print('NOT 200')
        return

    return response.json()['error'] == 0

def SearchProducts(keyword):
    global cookie
    response = requests.get(
        url=f'https://shopee.tw/api/v4/search/search_items?by=relevancy&keyword={urllib.parse.quote(keyword)}&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2',
        headers={
            'cookie': cookie,
            'referer': 'https://shopee.tw/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'x-api-source': 'pc',
            'x-csrftoken': 'NCaZXYtwXQOI7pth3q74h4msPjfYcsd6',
            'x-requested-with': 'XMLHttpRequest',
            'x-shopee-language': 'zh-Hant'
        }
    )
    if response.status_code != 200:
        print('NOT 200')
        return

    for item in response.json()['items']:
        item = item['item_basic']
        name = item['name']
        price_min = int(item['price_min'] / 100000)
        price_max = int(item['price_max'] / 100000)
        print(f'品名：{name}')
        print(f'價格：{price_min} ~ {price_max}')
        print('')

if __name__ == '__main__':
    res = CheckStatus()
    if res:
        print('登入成功')
        SearchProducts('iphone')
    else:
        print('登入失敗，請更換新的 Cookie')