from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



import time


def open_in_new_tab():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("https://yahoo.com")
    finance_path = driver.find_element(By.XPATH,'//a[@id = "root_3"]')
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(finance_path).key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[1])
    my_portfolio_path = driver.find_element(By.XPATH,'//a[@title="My Portfolio"]')
    my_portfolio_path.click()
    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    open_in_new_tab()
