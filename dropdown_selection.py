from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

import time


def select_dropdown():
    option = Options()
    option.headless = False
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=option)
    driver.maximize_window()
    driver.get("https://www.deerwalk.com/contact")
    state_path = driver.find_element(By.XPATH, '//select[@name="state"]')
    Select(state_path).select_by_visible_text("Alabama")
    time.sleep(5)


def select_dropdown2():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("https://www.deerwalk.com/contact")
    state_path = driver.find_element(By.XPATH, '//select[@name="state"]')
    state_path.click()

    time.sleep(5)


if __name__ == '__main__':
    select_dropdown()
    # select_dropdown2
