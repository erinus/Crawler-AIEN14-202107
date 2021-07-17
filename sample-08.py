import re

urls = [
    'https://www.momoshop.com.tw/search/searchShop.jsp?keyword=%E7%AD%86%E9%9B%BB%E9%85%8D%E4%BB%B6&searchType=6&cateLevel=0&cateCode=&curPage=1&_isFuzzy=0&showType=chessboardType',
    'https://24h.pchome.com.tw',
    'https://24h.pchome.com.tw/onsale/v4/20210717',
    'https://24h.pchome.com.tw/onsale/v4/20210717/#!ce.htm',
    'http://24h.pchome.com.tw/onsale/v4/20210717/#!ce.htm',
    'https://24h.pchome.com.tw:8080/onsale/v4/20210717/#!ce.htm'
]

def check(url):
    m = re.match(r'^https?://\w+(\.\w+)+(:\d{1,5})?(/\w+)*(\?\w+=\w+(\&\w+=\w+)*)?', url)
    print(m)
    return m is not None

for url in urls:
    print(f'{url}: {check(url)}')