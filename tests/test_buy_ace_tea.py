import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cart_page import Cart_page
from pages.checkout_page import Checkout_page
from pages.main_page import Main_page
from pages.product_page import Product_page
from pages.thank_page import Thank_page

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

def test_cmoke_buy_ace_tea():

        main = Main_page(driver)
        main.choose_ace_tea()

        product = Product_page(driver)
        product.add_product_in_cart_and_move_cart()

        cart = Cart_page(driver)
        cart.assert_text_cart()
        cart.click_checkout_button()

        checkout = Checkout_page(driver)
        time.sleep(5)
        checkout.assert_text_checkout_page()
        checkout.filling_checkout_form()

        thank = Thank_page(driver)
        time.sleep(5)
        thank.assert_text_word_thank_page()
