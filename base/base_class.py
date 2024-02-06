import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Base():
    def __init__(self, driver):
        self.driver = driver

    def scrool_to_element(self, locator):
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", locator)

    def assert_word(self, word, result):
        value_word = word
        assert value_word == result
        print('Проверка текста пройдена')

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Текущий url ' + '"' + get_url + '"')

    def screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\tester9000\\PycharmProjects\\pythonSeleniumEX\\screen\\' + name_screenshot)
        print('Сделали скриншот')
