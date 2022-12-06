from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time


def open_url():
    driver = webdriver.Chrome('C:\chromedriver.exe')
    driver.get("https://google.com")
    time.sleep(3)
    driver.quit()


def open_url2():
    s = Service('C:\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.get("https://google.com")
    time.sleep(3)
    driver.quit()


def open_url3():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://google.com")
    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    # open_url2()
    open_url3()
