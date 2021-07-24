import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def TestChrome():
    password = None
    with open('password.txt', 'r') as f:
        password = f.read()

    # mobile_emulation = { 'deviceName': 'Google Nexus 5' }

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # options.add_experimental_option('mobileEmulation', mobile_emulation)
    # options.add_argument('--kiosk')

    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.facebook.com/')

    # elm_input_email = driver.find_element_by_id('email')
    # elm_input_email = driver.find_element_by_css_selector('#email')
    elm_input_email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#email'))
    )
    elm_input_email.send_keys('erinus.startup@gmail.com')

    # elm_input_pass = driver.find_element_by_id('pass')
    # elm_input_pass = driver.find_element_by_css_selector('#pass')
    elm_input_pass = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#pass'))
    )
    elm_input_pass.send_keys(password)

    # elm_button_login = driver.find_element_by_css_selector('button[name="login"]')
    elm_button_login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[name="login"]'))
    )
    elm_button_login.click()

    # Android 手機接上 USB 傳輸線，透過 ADB 執行拍照後，將照片檔案用 pillow 影像處理套件打開，然後切圖，切出安全代碼的部分，再交給 pytesseract 光學影像文字辨識套件去做畫面上的數字辨識

    time.sleep(60)

    driver.quit()

if __name__ == '__main__':
    TestChrome()