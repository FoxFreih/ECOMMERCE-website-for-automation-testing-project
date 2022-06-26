import time

import pytest
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class TestLogInPage:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

        chrome_driver_binary = "./drivers/chromedriver"
        ser_chrome = ChromeService(chrome_driver_binary)
        self.driver = webdriver.Chrome(service=ser_chrome, options=options)
        yield self.driver
        self.driver.close()

    # def test_register_signUp(self):
    #     self.driver.get('https://demo.nopcommerce.com/')
    #     self.driver.maximize_window()
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a').click()
    #     time.sleep(1)
    #     self.driver.find_element(By.ID, "gender-female").click()
    #     time.sleep(1)
    #     self.driver.find_element(By.NAME,"FirstName").send_keys("Amal")
    #     time.sleep(1)
    #     self.driver.find_element(By.NAME, "LastName").send_keys("Saleh")
    #     time.sleep(1)
    #     Day = Select(self.driver.find_element(By.NAME, "DateOfBirthDay")).select_by_value('28')
    #     time.sleep(1)
    #     Month = Select(self.driver.find_element(By.NAME, "DateOfBirthMonth")).select_by_value('5')
    #     time.sleep(1)
    #     Year = Select(self.driver.find_element(By.NAME, "DateOfBirthYear")).select_by_value('1996')
    #     time.sleep(1)
    #     self.driver.find_element(By.NAME, "Email").send_keys("amalfreih96@gmail.com")
    #     time.sleep(1)
    #     self.driver.find_element(By.NAME, "Company").send_keys("apple")
    #     time.sleep(1)
    #     self.driver.find_element(By.NAME, "Password").send_keys("Amal1996*")
    #     time.sleep(1)
    #     self.driver.find_element(By.NAME, "ConfirmPassword").send_keys("Amal1996*")
    #     time.sleep(1)
    #
    #     register_button = self.driver.find_element(By.NAME, 'register-button').click()
    #
    #     time.sleep(5)
    #
    # def test_positive_login(self):
    #     self.driver.get('https://demo.nopcommerce.com/')
    #     time.sleep(1)
    #     self.driver.maximize_window()
    #     self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a').click()
    #     time.sleep(1)
    #     email = "amalfreih96@gmail.com"
    #     self.driver.find_element(By.NAME,"Email").send_keys(email)
    #     time.sleep(1)
    #     self.driver.find_element(By.NAME, "Password").send_keys("Amal1996*")
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button').click()
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a").click()
    #     time.sleep(1)
    #     text = self.driver.find_element(By.NAME, "Email").get_attribute("value")
    #     # time.sleep(2)
    #     assert text == email

    # def test_negative_login(self):
    #     self.driver.get('https://demo.nopcommerce.com/')
    #     time.sleep(1)
    #     self.driver.maximize_window()
    #     self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a').click()
    #     time.sleep(1)
    #     self.driver.find_element(By.NAME,"Email").send_keys("abcd@gmail.com")
    #     time.sleep(1)
    #     self.driver.find_element(By.NAME, "Password").send_keys("Amal1996*")
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button').click()
    #     time.sleep(1)
    #
    #     error_message1 = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[1]").text
    #     error_message2 = self.driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[1]/ul/li").text
    #     assert error_message1  or error_message2 in "Login was unsuccessful. Please correct the errors and try again.\nNo customer account found"

    def test_error_messages_for_mandatory_fields(self):
        self.driver.get('https://demo.nopcommerce.com/')
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a').click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "Email").send_keys("amalfreih96@gmail.com")
        time.sleep(1)
        self.driver.find_element(By.NAME, 'register-button').click()
        time.sleep(5)
        first_name = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[2]/span[2]/span').text
        last_name = self.driver.find_element(By.XPATH,
                                              '/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[3]/span[2]/span').text
        password = self.driver.find_element(By.XPATH,
                                             '/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[4]/div[2]/div[1]/span[2]/span').text
        confirm_password = self.driver.find_element(By.XPATH,
                                            '/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[4]/div[2]/div[2]/span[2]/span').text
        error_messages = {'First name is required.','Last name is required.','Password is required.'}

        assert {first_name, last_name, password, confirm_password}.issubset(error_messages)


    def test_error_messages_for_entering_incorrect_values_in_fields(self):
        self.driver.get('https://demo.nopcommerce.com/')
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a').click()
        time.sleep(1)
        self.driver.find_element(By.ID, "gender-female").click()
        time.sleep(1)
        self.driver.find_element(By.NAME,"FirstName").send_keys("Amal")
        time.sleep(1)
        self.driver.find_element(By.NAME, "LastName").send_keys("Saleh")
        time.sleep(1)
        Day = Select(self.driver.find_element(By.NAME, "DateOfBirthDay")).select_by_value('28')
        time.sleep(1)
        Month = Select(self.driver.find_element(By.NAME, "DateOfBirthMonth")).select_by_value('5')
        time.sleep(1)
        Year = Select(self.driver.find_element(By.NAME, "DateOfBirthYear")).select_by_value('1996')
        time.sleep(1)
        self.driver.find_element(By.NAME, "Email").send_keys("amalfreih.com")
        time.sleep(2)
        self.driver.find_element(By.NAME, "Company").send_keys("Apple")
        time.sleep(1)
        self.driver.find_element(By.NAME, "Password").send_keys("*")
        time.sleep(1)
        self.driver.find_element(By.NAME, "ConfirmPassword").send_keys("*23")
        time.sleep(1)
        register_button = self.driver.find_element(By.NAME, 'register-button').click()

        email_error = self.driver.find_element(By.CSS_SELECTOR, "body > div.master-wrapper-page > div.master-wrapper-content > div > div > div > div.page-body > form > div:nth-child(1) > div.form-fields > div:nth-child(5) > span.field-validation-error")
        time.sleep(2)

        password_error = self.driver.find_element(By.CSS_SELECTOR, "body > div.master-wrapper-page > div.master-wrapper-content > div > div > div > div.page-body > form > div:nth-child(4) > div.form-fields > div:nth-child(1) > span.field-validation-error")
        time.sleep(2)
        confirm_password_error = self.driver.find_element(By.CSS_SELECTOR, "body > div.master-wrapper-page > div.master-wrapper-content > div > div > div > div.page-body > form > div:nth-child(4) > div.form-fields > div:nth-child(2) > span.field-validation-error")
        time.sleep(1)
        print("email_error:\n", email_error.text)
        print(email_error.get_attribute("class"))
        print("password_error:", password_error.text)
        print(password_error.get_attribute("class"))
        print("confirm_password_error:", confirm_password_error.text)
        print(confirm_password_error.get_attribute("class"))
        assert "error" in email_error.get_attribute("class") and password_error.get_attribute("class") and confirm_password_error.get_attribute("class")


        time.sleep(5)

    def test_search_product(self):
        self.driver.get('https://demo.nopcommerce.com/')
        self.driver.maximize_window()
        time.sleep(1)
        actions = ActionChains(self.driver)
        electronics = self.driver.find_element(By.CSS_SELECTOR, "body > div.master-wrapper-page > div.header-menu > ul.top-menu.notmobile > li:nth-child(2) > a")
        time.sleep(2)
        actions.move_to_element(electronics).perform()
        time.sleep(2)
        camera_photo_products = self.driver.find_element(By.CSS_SELECTOR, "body > div.master-wrapper-page > div.header-menu > ul.top-menu.notmobile > li:nth-child(2) > ul > li:nth-child(1) > a")
        time.sleep(2)
        actions.move_to_element(camera_photo_products).click().perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                               "body > div.master-wrapper-page > div.master-wrapper-content > div > div.center-2 > div > div.page-body > div.products-container > div.products-wrapper > div > div > div:nth-child(1) > div > div.details > h2 > a").click()
        product_text = self.driver.find_element(By.CSS_SELECTOR, "#product-details-form > div:nth-child(2) > div.product-essential > div.overview > div.product-name > h1").text

        self.driver.find_element(By.CSS_SELECTOR, "#small-searchterms").send_keys(product_text)
        self.driver.find_element(By.CSS_SELECTOR, "#small-search-box-form > button").click()
        search_text = self.driver.find_element(By.CSS_SELECTOR, "body > div.master-wrapper-page > div.master-wrapper-content > div > div.center-2 > div > div.page-body > div.search-results > div > div.products-wrapper > div > div > div > div > div.details > h2 > a").text

        print("product_text:",product_text,"\nsearch_text:", search_text)
        assert search_text == product_text

    def test_end_to_end_buy_product(self):
        self.driver.get('https://demo.nopcommerce.com/')
        self.driver.maximize_window()
        time.sleep(1)
        actions = ActionChains(self.driver)
        shoes = self.driver.find_element(By.CSS_SELECTOR, "body > div.master-wrapper-page > div.header-menu > ul.top-menu.notmobile > li:nth-child(3) > a")
        time.sleep(4)
        actions.move_to_element(shoes).perform()
        time.sleep(4)
        shoes_products = self.driver.find_element(By.CSS_SELECTOR, "body > div.master-wrapper-page > div.header-menu > ul.top-menu.notmobile > li:nth-child(3) > ul > li:nth-child(1) > a")
        time.sleep(4)
        actions.move_to_element(shoes_products).click().perform()
        time.sleep(4)
        self.driver.find_element(By.CSS_SELECTOR, "body > div.master-wrapper-page > div.master-wrapper-content > div > div.center-2 > div > div.page-body > div.products-container > div.products-wrapper > div > div > div:nth-child(2) > div > div.details > h2 > a").click()
        time.sleep(2)
        Select(self.driver.find_element(By.NAME, "product_attribute_6")).select_by_value('13')
        time.sleep(2)
        Select(self.driver.find_element(By.NAME, "product_attribute_7")).select_by_value('18')
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#image-squares-8 > li:nth-child(1) > label > span > span").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#product_enteredQuantity_24").clear()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,"#product_enteredQuantity_24").send_keys("2")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-button-24").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#bar-notification > div > span").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#topcartlink > a > span.cart-label").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#termsofservice").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#Email").send_keys("amalfreih96@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#Password").send_keys("Amal1996*")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "body > div.master-wrapper-page > div.master-wrapper-content > div > div > div > div.page-body > div.customer-blocks > div.returning-wrapper.fieldset > form > div.buttons > button").click()
        time.sleep(4)
        self.driver.find_element(By.CSS_SELECTOR, "#termsofservice").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        time.sleep(4)
        Select(self.driver.find_element(By.NAME, "BillingNewAddress.CountryId")).select_by_value('149')
        time.sleep(2)
        self.driver.find_element(By.NAME, "BillingNewAddress.City").send_keys("Rahat")
        time.sleep(2)
        self.driver.find_element(By.NAME, "BillingNewAddress.Address1").send_keys("Alhaj, 9")
        time.sleep(2)
        self.driver.find_element(By.NAME, "BillingNewAddress.ZipPostalCode").send_keys("8535700")
        time.sleep(2)
        self.driver.find_element(By.NAME, "BillingNewAddress.PhoneNumber").send_keys("+972529523453")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#billing-buttons-container > button.button-1.new-address-next-step-button").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#shipping-method-buttons-container > button").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "paymentmethod_0").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#payment-method-buttons-container > button").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#payment-info-buttons-container > button").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#confirm-order-buttons-container > button").click()
        time.sleep(2)
        text = self.driver.find_element(By.CSS_SELECTOR, "body > div.master-wrapper-page > div.master-wrapper-content > div > div > div > div.page-body.checkout-data > div > div.title > strong").text
        assert text == "Your order has been successfully processed!"

    def test_add_to_Wishlist(self):
        self.driver.get('https://demo.nopcommerce.com/')
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "body > div.master-wrapper-page > div.header-menu > ul.top-menu.notmobile > li:nth-child(6) > a").click()
        time.sleep(4)
        product_name = self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.master-wrapper-page > div.master-wrapper-content > div > div.center-2 > div > div.page-body > div.products-container > div.products-wrapper > div > div > div:nth-child(2) > div > div.details > h2 > a").text

        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[6]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/div[2]/button[3]").click()
        time.sleep(2)

        success_message = self.driver.find_element(By.XPATH,
                                 "/html/body/div[5]/div/p").text
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[5]/div/span").click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[3]/a/span[1]").click()
        time.sleep(4)
        wish_list_product_name = self.driver.find_element(By.XPATH,
                                                   "/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/form/div[1]/table/tbody/tr/td[4]/a").text
        time.sleep(2)

        assert wish_list_product_name == product_name and success_message == 'The product has been added to your wishlist'

    def test_total_price_reflects_correctly_with_changes_quantity_on_shopping_cart(self):
        self.driver.get('https://demo.nopcommerce.com/')
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.master-wrapper-page > div.header-menu > ul.top-menu.notmobile > li:nth-child(6) > a").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/div[2]/button[1]").click()
        #
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[5]/div/span").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[4]/a/span[1]").click()
        time.sleep(6)
        self.driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/div/form/div[1]/table/tbody/tr/td[5]/input").clear()
        time.sleep(2)
        e = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/div/form/div[1]/table/tbody/tr/td[5]/input")
        # time.sleep(5)
        e.send_keys('2')
        e.send_keys(Keys.ENTER)
        # self.driver.find_element(By.NAME, "updatecart").click()
        time.sleep(5)
        unit_price = self.driver.find_element(By.CSS_SELECTOR, "#shopping-cart-form > div.table-wrapper > table > tbody > tr > td.unit-price > span").text
        unit_price= unit_price[1:]
        # float(unit_price)
        print("\nUnit price:",unit_price)
        time.sleep(2)
        total_price = self.driver.find_element(By.CSS_SELECTOR, "#shopping-cart-form > div.table-wrapper > table > tbody > tr > td.subtotal > span").text
        total_price = total_price[1:]
        # float(total_price)
        print("\n Total price:",total_price)

        assert float(unit_price)*2 == float(total_price)












