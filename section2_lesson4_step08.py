# https://stepik.org/lesson/181384/step/8?unit=156009

from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    browser.find_element_by_xpath("//button[@id='book']").click()

    x_element = browser.find_element_by_xpath("//label/span[2]")
    x = x_element.text
    y = calc(x)

    browser.find_element_by_xpath("//input").send_keys(y)

    browser.find_element_by_xpath("//button[@id='solve']").click()

finally:
    time.sleep(5)
    browser.quit()