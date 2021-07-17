import requests
import pyquery

def GetProduct(pid):
    response = requests.get(
        url=f'https://www.books.com.tw/products/{pid}',
        headers={
            'referer': f'https://www.books.com.tw/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    )
    if response.status_code != 200:
        print('not 200')
        return

    with open('books.html', 'wb') as f:
        f.write(response.content)

    doc = pyquery.PyQuery(response.text)
    elm_h1 = doc('div.container_24 > div.grid_20 div.omega h1')
    print(elm_h1.text())
    elm_strong = doc('div.container_24 > div.grid_20 div.omega ul.price > li > strong')
    print(elm_strong.text())

if __name__ == '__main__':
    pid = 'N001191044'
    GetProduct(pid)