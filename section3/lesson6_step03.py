# https://stepik.org/lesson/237240/step/3?unit=209628

import time
import math
import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.mark.parametrize('address', ["236895", "236896", "236897", "236898", "236899", "236903", "236903", "236905"])
def test_check_feedback(browser, address):
    link = f"https://stepik.org/lesson/{address}/step/1"
    browser.get(link)

    answer = math.log(int(time.time()))

    browser.find_element_by_css_selector(".ember-text-area").send_keys(str(answer))
    browser.find_element_by_css_selector(".submit-submission").click()

    feedback = browser.find_element_by_css_selector(".smart-hints__hint").text

    assert feedback == "Correct!", f"{feedback}"
