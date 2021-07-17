import re

print(re.match(r'^\d?$', '1'))
print(re.match(r'^\d?', '1ABC'))
print(re.match(r'^\d?', 'ABC'))
print(re.match(r'^\d?', '12ABC'))
print(re.match(r'^\d?A', '12ABC'))
print(re.match(r'^\d{0,2}A', '12ABC'))