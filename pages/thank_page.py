import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Thank_page(Base):


    def __init__(self, driver):
        super().__init__(driver)

# Locators

    text_thank_page = '//div[@class="sc-6f65eba9-0 cEiXhI sc-92c9b6a9-1 fdAGqE"]'


    # Getters

    def get_word_thank_page(self):
        elements = self.driver.find_elements(By.XPATH, self.text_thank_page)
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.text_thank_page)))

    # Actions

    def text_word_thank_page(self):
        text = self.get_word_thank_page().text
        print('Мы находимся на странице c Благодарностью за заказ')
        return text

    # Methods

    def assert_text_word_thank_page(self):
        self.assert_word(self.text_word_thank_page(), 'Спасибо за заказ!')
        self.get_current_url()
        self.screenshot()