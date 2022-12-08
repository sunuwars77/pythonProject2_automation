import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def read_excel_file():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    reader = pd.read_excel('url/qa_automation1.xlsx')
    for row, column in reader.iterrows():
        sn = column["SN"]
        url = column["URL"]
        site_name = column["Site Name"]
        driver.get(url)
        actual_title = driver.title
        expected_title = site_name
        print(actual_title)
        print(expected_title)
        try:
            assert expected_title in actual_title
        except AssertionError:
            print(sn,url,site_name,"title dont match")
        else:
            print(sn,url,site_name,"title match")
        time.sleep(1)
    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    read_excel_file()
