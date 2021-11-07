import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_for_button_presence(browser):
    browser.get(link)
    time.sleep(3)
    assert len(browser.find_elements_by_css_selector('[class="btn btn-lg btn-primary btn-add-to-basket"]')) == 1
