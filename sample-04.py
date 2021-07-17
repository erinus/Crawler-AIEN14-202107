import urllib.parse

text = '筆電配件'

encoded = urllib.parse.quote(text)
print(encoded)

decoded = urllib.parse.unquote(encoded)
print(decoded)