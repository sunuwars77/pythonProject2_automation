import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def read_excel():
    reader = pd.read_excel('url/automation_framework.xlsx')
    for row, column in reader.iterrows():
        sn = column["sn"]
        test_summary = column["test_summary"]
        xpath = column["xpath"]
        action = column["action"]
        value = column["value"]
        action_defination(sn, test_summary, xpath, action, value)


def action_defination(sn, test_summary, xpath, action, value):
    if action == 'open_browser':
        result, remarks = open_browser(value)
    elif action == 'open_url':
        result, remarks = open_url(value)
    elif action == 'click':
        result, remarks = click(xpath)
    elif action == 'compare_text':
        result, remarks = compare_text(xpath, value)
    elif action == 'input_text':
        result, remarks = input_text(xpath, value)
    elif action == 'new_tab':
        result,remarks = new_tab(xpath, value)
    elif action == 'select_dropdown':
        result, remarks = select_dropdown(xpath, value)
    elif action == 'close_browser':
        result, remarks = close_browser()
    elif action == 'wait':
        result, remarks = wait(value)
    else:
        result = "FAIL"
        remarks = (action, "Not Supported")
    print(sn, test_summary, result, remarks)


def wait(value):
    try:
        time.sleep(value)
        result = "PASS"
        remarks = ""
    except Exception as ex:
        result = "FAIL"
        remarks = ex
    return result, remarks


def new_tab(xpath, value):
    try:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://google.com")
        result = "PASS"
        remarks = ""
    except Exception as ex:
        result = "FAIL"
        remarks = ex
    return result, remarks


def open_browser(value):
    try:
        global driver
        if value == 'chrome':
            s = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=s)
            driver.maximize_window()
            result = "PASS"
            remarks = ""
        elif value == 'firefox':
            print("Firefox code here")
            result = "PASS"
            remarks = ""
        else:
            result = "FAIL"
            remarks = (value, "Browser Not Supported")
    except Exception as ex:
        result = "FAIL"
        remarks = ex
    return result, remarks


def open_url(value):
    try:
        driver.get(value)
        result = "PASS"
        remarks = ""
    except Exception as ex:
        result = "FAIL"
        remarks = ex
    return result, remarks


def click(xpath):
    try:
        driver.find_element(By.XPATH, xpath).click()
        result = "PASS"
        remarks = ""
    except Exception as ex:
        result = "FAIL"
        remarks = ex
    return result, remarks


def input_text(xpath, value):
    try:
        driver.find_element(By.XPATH, xpath).send_keys(value)
        result = "PASS"
        remarks = ""
    except Exception as ex:
        result = "FAIL"
        remarks = ex
    return result, remarks


def compare_text(xpath, value):
    try:
        actual_text = driver.find_element(By.XPATH, xpath).text
        try:
            assert actual_text == value
        except AssertionError:
            result = "FAIL"
            remarks = ("Actual value is",actual_text,"Expected value is",value)
        else:
            result = "PASS"
            remarks = ""
    except Exception as ex:
        result = "FAIL"
        remarks = ex
    return result, remarks


def select_dropdown(xpath, value):
    try:
        state_path = driver.find_element(By.XPATH, xpath)
        Select(state_path).select_by_visible_text(value)
        result = "PASS"
        remarks = ""
    except Exception as ex:
        result = "FAIL"
        remarks = ex
    return result, remarks


def close_browser():
    try:
        driver.quit()
        result = "PASS"
        remarks = ""
    except Exception as ex:
        result = "FAIL"
        remarks = ex
    return result, remarks


if __name__ == "__main__":
    read_excel()