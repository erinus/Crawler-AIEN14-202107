import datetime

import requests
import chardet

def GetStockDailyInfo(stock):
    # date = datetime.datetime.now().strftime('%Y%m%d')
    # response = requests.get(
    #     url=f'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=csv&date={date}&stockNo={stock}',
    #     headers={
    #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    #     }
    # )
    # if response.status_code != 200:
    #     print('NOT 200')
    #     return

    # with open('stock.csv', 'wb') as f:
    #     f.write(response.content)

    # res = chardet.detect(response.content)
    content = None
    with open('stock.csv', 'rb') as f:
        content = f.read()
    res = chardet.detect(content)

    if res['confidence'] < 0.7:
        print('UNKNOWN ENCODING')
        return

    # print(response.content.decode(res['encoding']))
    data = content.decode(res['encoding'])
    lines = data.split('\n')
    lines = lines[2:-6]
    # print('\n'.join(lines))

    for line in lines:
        cells = line.split('","')
        cells[0] = cells[0][1:]
        cells[-1] = cells[-1][:-3]
        cells = [
            cell.replace(',', '')
            for cell in cells
        ]
        print(cells)

if __name__ == '__main__':
    stock = '2330'
    GetStockDailyInfo(stock)