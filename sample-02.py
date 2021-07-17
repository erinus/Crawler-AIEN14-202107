import json

text = '{"name":"john","age":25}'
d = json.loads(text)
print(d)

d['age'] = 27
print(d)

prices = [200, 210, 230.5]
text = json.dumps(prices)
print(text)