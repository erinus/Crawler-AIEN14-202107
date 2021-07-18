import requests
import pyquery

def GetIndex():
    response = requests.get(
        url='https://shopee.tw/api/v2/user/account_info?from_wallet=false&skip_address=1&need_cart=1',
        headers={
            'cookie': '<請輸入自己在瀏覽器上登入後的 Cookie>',
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

    print(response.text)

if __name__ == '__main__':
    GetIndex()