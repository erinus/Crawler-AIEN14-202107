import json

import requests

def GetYoubikeSites():
    response = requests.get(
        url='https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json',
        headers={
            'referer': f'https://www.google.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    )
    if response.status_code != 200:
        print('NOT 200')
        return

    sites = json.loads(response.text)
    for site in sites:
        name = site['sna']
        available = site['sbi']
        print(f'{name}: {available}')

if __name__ == '__main__':
    GetYoubikeSites()