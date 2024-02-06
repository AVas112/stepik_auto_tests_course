import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Checkout_page(Base):


    def __init__(self, driver):
        super().__init__(driver)

# Locators

    text_checkout_page = '//div[@class="sc-6f65eba9-0 cEiXhI sc-df1a5a68-1 gJmXBJ"]'
    field_entrance = '//input[@name="entrance"]'
    field_floor = '//input[@name="floor"]'
    field_apartment = '//input[@name="apartment"]'
    field_intercom = '//input[@name="intercom"]'
    choice_time = '(//div[@color="black" and @class="sc-6f65eba9-0 cOjGbJ"])[19]'
    field_phone = '//input[@autocomplete="tel"]'
    field_name = '//input[@name="name"]'
    field_mail = '(//input[@name="email"])[1]'
    field_comment = '//textarea[@name="comment"]'
    button_send_order = '(//div[@class="sc-6f65eba9-0 jEKBdg sc-3d8576a0-3 dScSzk"])[4]'

    # Getters

    def get_word_checkout_page(self):
        elements = self.driver.find_elements(By.XPATH, self.text_checkout_page)
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.text_checkout_page)))

    def get_field_entrance(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_entrance)))

    def get_field_floore(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_floor)))

    def get_field_apartment(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_apartment)))

    def get_field_intercom(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_intercom)))

    def get_choice_time(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choice_time)))

    def get_field_phone(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_phone)))

    def get_field_name(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_name)))

    def get_field_mail(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_mail)))

    def get_field_comment(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_comment)))

    def get_button_send_order(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_send_order)))


    # Actions

    def text_word_checkout_page(self):
        text = self.get_word_checkout_page().text
        print('Мы находимся на странице Оформление заказа')
        return text

    def input_field_entrance(self):
        self.get_field_entrance().send_keys('1')
        print('Ввели номер подъезда')

    def input_field_floore(self):
        self.get_field_floore().send_keys('2')
        print('Ввели номер этажа')

    def input_field_apartment(self):
        self.get_field_apartment().send_keys('3')
        print('Ввели номер квартиры')

    def input_field_intercom(self):
        self.get_field_intercom().send_keys('#0000#')
        print('Ввели код от домофона')

    def click_choice_time(self):
        self.get_choice_time().click()
        print('Выбрали время доставки')

    def input_field_phone(self):
        self.get_field_phone().send_keys('88005553535')
        print('Ввели номер телефона')

    def input_field_name(self):
        self.get_field_name().send_keys('Андрей')
        print('Ввели имя')

    def input_field_mail(self):
        self.get_field_mail().send_keys('test@test.ru')
        print('Ввели почту')

    def input_field_comment(self):
        self.get_field_name().send_keys('Комментарий к заказу')
        print('Ввели комментарий к заказу')

    def click_button_send_order(self):
        self.get_button_send_order().click()
        print('Кликнули по кнопке оформить заказ')

    # Methods

    def assert_text_checkout_page(self):
        self.assert_word(self.text_word_checkout_page(), 'Оформление заказа')

    def filling_checkout_form(self):
        time.sleep(5)
        self.get_current_url()
        self.input_field_entrance()
        self.input_field_floore()
        self.input_field_apartment()
        self.input_field_intercom()
        self.click_choice_time()
        self.input_field_phone()
        self.input_field_name()
        self.input_field_mail()
        self.input_field_comment()
        self.click_button_send_order()
