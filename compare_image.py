from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from PIL import Image, ImageChops, ImageStat

import glob
import os

input_logo = 'input/input1.png'
output_logo = 'output/output.png'
comparison_result = 'output/result.png'


def clear_result():
    files = glob.glob('output/*')
    for i in files:
        os.remove(i)


def capture_image():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("https://google.com")
    with open(output_logo, 'wb') as file:
        file.write(
            driver.find_element(By.XPATH, '//img[contains(@src,"/images/branding/googlelogo/")]').screenshot_as_png)
        img1 = Image.open(input_logo)
        img2 = Image.open(output_logo)
        logoresult = ImageChops.difference(img1, img2)
        stat = ImageStat.Stat(logoresult)
        diff_value = sum(stat.mean)
        print('value is', diff_value)
        if diff_value > 1:
            result = "fail"
        else:
            result = "pass"
        print(result)
        logoresult.show()
        logoresult.save(comparison_result)


if __name__ == '__main__':
    clear_result()
    capture_image()
