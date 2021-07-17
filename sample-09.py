import re

url = 'https://24h.pchome.com.tw/prod/DPADS4-A9009M974'

m = re.match(r'^https://\w+(\.\w+)+/prod/([-\w]+)', url)
print(m.groups(0)[1])

m = re.match(r'^https://\w+(\.\w+)+/prod/(?P<pid>[-\w]+)', url)
print(m.group('pid'))