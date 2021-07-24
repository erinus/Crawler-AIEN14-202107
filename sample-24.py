import requests
import pyquery

def GetData(proxies):
    print('GetData')
    for proxy in proxies:
        try:
            response = requests.get('https://24h.pchome.com.tw', proxies=proxy, timeout=5)
            if response.status_code != 200:
                print('NOT 200')
                continue
            print(response.text)
        except Exception as e:
            print(e)
            continue
        break

def GetProxies():
    response = requests.get('https://free-proxy-list.net/')
    if response.status_code != 200:
        print('NOT 200')
        return

    doc = pyquery.PyQuery(response.text)
    elm_textarea = doc('textarea')
    txt_textarea = elm_textarea.text()

    lines = txt_textarea.split('\n')
    lines = lines[3:-1]
    # txt_textarea = '\n'.join(lines)
    # print(txt_textarea)

    proxies = []
    for line in lines:
        http_proxy = f'http://{line}'
        https_proxy = f'https://{line}'
        # print(f'HTTP: {http_proxy}')
        # print(f'HTTPS: {https_proxy}')
        # print('')
        proxies.append({
            'http': http_proxy,
            'https': https_proxy
        })

    GetData(proxies)

if __name__ == '__main__':
    GetProxies()