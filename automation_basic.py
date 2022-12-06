from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time


def open_url():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("https://google.com")
    google_in_nepali = driver.find_element(By.XPATH, '//div[@id="SIvCob"]')
    actual_text = google_in_nepali.text
    expected_text = "Google यी भाषामा उपलब्ध छ: English"
    try:
        assert actual_text == expected_text
    except AssertionError:
        print("footer text comparion test fail")
    else:
        print("footer text comparison pass")

    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(actual_text)
    search_button = driver.find_element(By.XPATH, '//div[@class="FPdoLc lJ9FBc"]/center/input[@name="btnK"]')
    search_button.click()
    time.sleep(1)
    actual_title = driver.title
    expected_title = "Nepal - Google खोजी"
    try:
        assert actual_title == expected_title
    except AssertionError:
        print("title  comparion fail")
    else:
        print("title comparison pass")

    driver.quit()


if __name__ == '__main__':
    open_url()
