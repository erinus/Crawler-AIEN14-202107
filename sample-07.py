import re

emails = [
    'test@gmail',
    'test@gmail.com',
    'test@gmail.com.tw',
    'test@test.gmail.com.tw'
]

def check(email):
    return re.match(r'^\w+@\w+(\.\w+)+$', email) is not None

for email in emails:
    print(f'{email}: {check(email)}')