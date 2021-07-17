import urllib.parse

url = 'https://24h.pchome.com.tw/prod/DPADS4-A9009M974'
res = urllib.parse.urlparse(url)
print(res)
print(res.path)
print(res.path[6:])
print(res.path.replace('/prod/', ''))

url = 'https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=9009069'
res = urllib.parse.urlparse(url)
print(res)
print(res.path)
print(res.query)
print(res.query[7:])
print(res.query.replace('i_code=', ''))
pair = res.query.split('=')
if pair[0] == 'i_code':
    print(pair[1])