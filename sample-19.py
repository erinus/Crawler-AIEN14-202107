import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def TestChrome():
    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/')

    time.sleep(5)

    driver.quit()

if __name__ == '__main__':
    TestChrome()