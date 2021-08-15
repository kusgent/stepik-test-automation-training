# https://stepik.org/lesson/36285/step/13?unit=162401

from selenium import webdriver
import unittest

class TestReg(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(1)
        browser.get("http://suninjuly.github.io/registration1.html")

        browser.find_element_by_css_selector(".first_block .first").send_keys("Ilya")
        browser.find_element_by_css_selector(".first_block .second").send_keys("Kustov")
        browser.find_element_by_css_selector(".first_block .third").send_keys("test@test.com")

        browser.find_element_by_css_selector("button.btn").click()

        welcome_text = browser.find_element_by_tag_name("h1").text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "The expected welcome text was not found!")

    def test_reg2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        browser.find_element_by_css_selector(".first_block .first").send_keys("Ilya")
        browser.find_element_by_css_selector(".first_block .second").send_keys("Kustov")
        browser.find_element_by_css_selector(".first_block .third").send_keys("test@test.com")

        browser.find_element_by_css_selector("button.btn").click()

        welcome_text = browser.find_element_by_tag_name("h1").text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "The expected welcome text was not found!")

if __name__ == "__main__":
    unittest.main()
