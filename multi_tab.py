from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time


def open_url():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("https://yahoo.com")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://google.com")
    driver.switch_to.window(driver.window_handles[0])
    driver.get("https://fifa.com")
    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    open_url()
