from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def open_url():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://saayog.com")
    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    open_url()
