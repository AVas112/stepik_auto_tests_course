import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Product_page(Base):


    def __init__(self, driver):
        super().__init__(driver)


    # Locators

    add_to_cart_button = '//div[text()="В корзину"]'
    cart_button = '(//a[@class="sc-699203a5-0 gZdCPf"])[5]'
    confir_adress = '//div[@class="sc-36710736-0 kUepil sc-3d8576a0-4 sc-3d8576a0-5 bnFHKR ipfKjZ sc-a98bcb5e-0 jhllwv"]'

    # Getters

    def get_add_to_cart_button(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_cart_button(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_confir_adress(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confir_adress)))

    # Actions

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print('Добавили товар в корзину')

    def click_cart_button(self):
        self.get_cart_button().click()
        print('Перешли в корзину')

    def click_confir_adress(self):
        self.get_confir_adress().click()
        print('Подтвердили адрес доставки')

    # Methods

    def add_product_in_cart_and_move_cart(self):
        self.click_add_to_cart_button()
        self.get_current_url()
        self.screenshot()
        time.sleep(5)
        self.click_confir_adress()
        time.sleep(5)
        self.click_cart_button()
        time.sleep(5)
