import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def csv_url_reader(obj):
    reader = csv.DictReader(obj, delimiter=',')
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()

    for line in reader:
        url = line["URL"]
        title = line["Title"]
        driver.get(url)
        print(driver.title, title)
        assert title in driver.title
        time.sleep(4)
    driver.quit()


if __name__ == "__main__":
    with open("URL.csv") as obj:

        csv_url_reader(obj)
