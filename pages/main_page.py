import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    url = 'https://www.cantata.ru/'

    def __init__(self, driver):
        super().__init__(driver)


    # Locators

    category_tea = '(//a[contains(text(),"Чай")])[1]'
    all_tea = '(//div[@class="sc-6f65eba9-0 bwJvI sc-de0862c5-3 ifKzgl"])[1]'
    filter_all_tea = '//div[@color="black_40" and @class="sc-6f65eba9-0 gvAFLg"]'
    filter_open_type_tea = '//div[contains(text(),"Вид чая")]'
    filter_type_tea = '(//div[@color="black" and @class="sc-6f65eba9-0 fEFyNw sc-433f1490-2 ipqunh"])[1]'
    filter_open_taste_tea = '//div[contains(text(),"Вкус")]'
    filter_taste_tea = '(//div[@color="black" and @class="sc-6f65eba9-0 fEFyNw sc-433f1490-2 ipqunh"])[21]'
    filter_open_ingredients_tea = '//div[contains(text(),"Ингредиенты в составе")]'
    filter_ingredients_tea = '(//div[@color="black" and @class="sc-6f65eba9-0 fEFyNw sc-433f1490-2 ipqunh"])[29]'
    ace_tea = '//a[@href="/item/kholodnyy-chay-napitok-faraonov-300-ml"]'


    # Getters

    def get_category_tea(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_tea)))

    def get_all_tea(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.all_tea)))

    def get_filter_all_tea(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_all_tea)))

    def get_filter_open_type_tea(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_open_type_tea)))

    def get_filter_type_tea(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_type_tea)))

    def get_filter_open_taste_tea(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_open_taste_tea)))

    def get_filter_taste_tea(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_taste_tea)))

    def get_filter_open_ingredients_tea(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_open_ingredients_tea)))

    def get_filter_ingredients_tea(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_ingredients_tea)))

    def get_ace_tea(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ace_tea)))

    # Actions

    def click_category_tea(self):
        self.get_category_tea().click()
        print('Перешли в категорию чая')

    def click_all_tea(self):
        self.get_all_tea().click()
        print('Выбрали весь чай')

    def click_filter_all_tea(self):
        self.get_filter_all_tea().click()
        print('В фильтре выбрали весь чай')

    def click_filter_open_type_tea(self):
        self.get_filter_open_type_tea().click()
        print('В фильтре открыли Вид чая')

    def click_filter_type_tea(self):
        self.get_filter_type_tea().click()
        print('В фильтре выбрали Айс Чай')

    def click_filter_open_taste_tea(self):
        self.get_filter_open_taste_tea().click()
        print('В фильтре выбрали Вкус чая')

    def click_filter_taste_tea(self):
        self.get_filter_taste_tea().click()
        print('Выбрали фруктовый вкус чая')

    def click_filter_open_ingredients_tea(self):
        self.get_filter_open_ingredients_tea().click()
        print('В фильтре выбрали ингридиент чая')

    def click_filter_ingredients_tea(self):
        self.get_filter_ingredients_tea().click()
        print('Выбрали апельсиновые ингридиенты чая')

    def click_ace_tea(self):
        self.get_ace_tea().click()
        print('Перешли на страницу Холодный чай «Напиток Фараонов», 300 мл')

    # Methods

    def choose_ace_tea(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.screenshot()
        self.get_current_url()
        self.click_category_tea()
        self.click_all_tea()
        self.scrool_to_element(self.get_filter_all_tea())
        self.click_filter_all_tea()
        self.click_filter_open_type_tea()
        self.click_filter_type_tea()
        self.click_filter_open_taste_tea()
        self.click_filter_taste_tea()
        self.click_filter_open_ingredients_tea()
        self.click_filter_ingredients_tea()
        self.click_ace_tea()


