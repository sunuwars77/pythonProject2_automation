from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time


def open_url():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("https://merolagani.com/ContactUs.aspx")
    full_name = driver.find_element(By.XPATH,'//input[contains(@id,"_txtFullName")]')
    full_name.send_keys("test user")
    mobile_number = driver.find_element(By.XPATH,'//input[contains(@id,"_txtMobileNo")]')
    mobile_number.send_keys("1234567890")
    email = driver.find_element(By.XPATH,'//input[contains(@id,"_txtEmail")]')
    email.send_keys("user@123gmail.com")
    message = driver.find_element(By.XPATH, '//textarea[contains(@id,"_txtMessage")]')
    message.send_keys("this is a test ")
    submit_button = driver.find_element(By.XPATH,'//a[contains(@id,"_lbtnSubmit")]')
    submit_button.click()
    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    open_url()
