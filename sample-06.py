import re

mobiles = [
    '0987654321',
    '0987-654321',
    '0987-654-321',
    '0987-654-31',
    '1987-654-31'
]

def check(mobile):
    return re.match(r'^09\d{2}-?\d{3}-?\d{3}', mobile) is not None

for mobile in mobiles:
    print(f'{mobile}: {check(mobile)}')