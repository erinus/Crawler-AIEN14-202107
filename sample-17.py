import urllib.parse

import requests
import pyquery

cookie = 'csrftoken=NCaZXYtwXQOI7pth3q74h4msPjfYcsd6; _fbp=fb.1.1610959964239.1214595128; __BWfp=c1610959964758x215d733ba; welcomePkgShown=true; REC_T_ID=88214394-596a-11eb-afbb-b4969186dd16; REC_T_ID=88523ed0-596a-11eb-8e96-48df37dd8805; SPC_F=g6DRkFw56U3Ss3xT4ERPzfWNeVTOtMJ4; G_ENABLED_IDPS=google; SPC_CLIENTID=ZzZEUmtGdzU2VTNTzslaoecxeunipkmo; _gcl_au=1.1.2068765182.1618821623; SPC_PC_HYBRID_ID=49; _med=refer; SPC_SSN=o; SPC_WSS=o; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.1558616491.1626586242; SPC_SI=mall.xKS4hrSgH5porFPIL0K7ZmsuFeHdN9kG; _dc_gtm_UA-61915057-6=1; SPC_ST=".c002OVNlSVFRR3pBZVZNUczE/PhYVpZDufiTMgPwAuZrPmPC7HRI4lv8FpeKkyraQrE8+pvuWlLt+zaWX55KE4ovJB0YMzizunbjBP8dYbzpsMZ7cjPJhnXU1R3/CYOFiDIfaX0Uu1k7uNI67cNw+PmOgnbtbo72LlGVdzJQ2Ns="; SPC_U=23359958; SPC_EC=Um5WMG5aY0lNdjh3SnI0eH2ksVVkVfY0pQE96A12W5pN9mpqpupTnngSU+GUM0J6v3Gmxk/9I8aZdZnORFYm3SJNMUP8+aYnHMdKW0HlleorIG8oIv//oJ6H8JqMdEqeU3B8+5qrfr2zV4r5hSSFIA==; SPC_IA=1; _ga=GA1.2.1758361101.1610959965; SPC_R_T_ID="qrqwkzRSvAtMN38vaYSS5JNNGHfZSRkoUT79xx2eaKb8YIT56QS0igp+oIta12HaKpCQ23aafkgfqBWOfHJsW2u2DmdSEVC/9E7nhnq353I="; SPC_T_IV="WrK0Hnaa+wN8v5L3TM2ZpQ=="; SPC_R_T_IV="WrK0Hnaa+wN8v5L3TM2ZpQ=="; SPC_T_ID="qrqwkzRSvAtMN38vaYSS5JNNGHfZSRkoUT79xx2eaKb8YIT56QS0igp+oIta12HaKpCQ23aafkgfqBWOfHJsW2u2DmdSEVC/9E7nhnq353I="; _ga_RPSBE3TQZZ=GS1.1.1626586241.20.1.1626589301.27'

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