import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)

# Locators

    word = '//div[@class="sc-6f65eba9-0 cEiXhI sc-df1a5a68-1 gJmXBJ"]'
    checkout_button = '(//div[@class="sc-6f65eba9-0 rSkSe sc-3d8576a0-3 dScSzk"])[1]'


    # Getters

    def get_word(self):
        elements = self.driver.find_elements(By.XPATH, self.word)
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.word)))

    def get_checkout_button(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    # Actions

    def text_word(self):
        text = self.get_word().text
        print('Мы находимся на странице Корзина')
        return text

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Кликнули по кнопке Оформить заказ')

    # Methods
    def assert_text_cart(self):
        self.assert_word(self.text_word(), 'Корзина')
        self.get_current_url()
        self.screenshot()

    def cart_click_checkout_button(self):
        self.click_checkout_button()
        time.sleep(7)