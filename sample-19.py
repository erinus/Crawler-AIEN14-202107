import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def TestChrome():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.facebook.com/')

    time.sleep(5)

    driver.quit()

if __name__ == '__main__':
    TestChrome()