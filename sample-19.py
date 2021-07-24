import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def TestChrome():
    # mobile_emulation = { 'deviceName': 'Google Nexus 5' }

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # options.add_experimental_option('mobileEmulation', mobile_emulation)
    # options.add_argument('--kiosk')

    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.facebook.com/')

    # elm_input_email = driver.find_element_by_id('email')
    elm_input_email = driver.find_element_by_css_selector('#email')
    elm_input_email.send_keys('<自己的帳號>')

    # elm_input_pass = driver.find_element_by_id('pass')
    elm_input_pass = driver.find_element_by_css_selector('#pass')
    elm_input_pass.send_keys('<自己的密碼>')

    elm_button_login = driver.find_element_by_css_selector('button[name="login"]')
    elm_button_login.click()

    time.sleep(60)

    driver.quit()

if __name__ == '__main__':
    TestChrome()