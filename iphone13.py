import time
import warnings
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains, Keys

class TestLogInPage:
    @pytest.fixture()
    def setup_method(self):
        chrome_options = ChromeOptions()
        ChromeOptions.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        chrome_driver_binary = r".\drivers\chromedriver.exe"
        chrome_options.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) "
                                    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
        ser_chrome = ChromeService(chrome_driver_binary)
        self.driver = webdriver.Chrome(service=ser_chrome, options=chrome_options)
        self.driver.set_window_size(414, 896)
        yield self.driver
        self.driver.close()


    def test_register_signUp(self):
        self.driver.get('https://demo.nopcommerce.com/')
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a').click()
        time.sleep(1)
        self.driver.find_element(By.ID, "gender-female").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "FirstName").send_keys("Amal")
        time.sleep(1)
        self.driver.find_element(By.NAME, "LastName").send_keys("Saleh")
        time.sleep(1)
        Day = Select(self.driver.find_element(By.NAME, "DateOfBirthDay")).select_by_value('28')
        time.sleep(1)
        Month = Select(self.driver.find_element(By.NAME, "DateOfBirthMonth")).select_by_value('5')
        time.sleep(1)
        Year = Select(self.driver.find_element(By.NAME, "DateOfBirthYear")).select_by_value('1996')
        time.sleep(1)
        self.driver.find_element(By.NAME, "Email").send_keys("amalfreih96@gmail.com")
        time.sleep(1)
        self.driver.find_element(By.NAME, "Company").send_keys("apple")
        time.sleep(1)
        self.driver.find_element(By.NAME, "Password").send_keys("Amal1996*")
        time.sleep(1)
        self.driver.find_element(By.NAME, "ConfirmPassword").send_keys("Amal1996*")
        time.sleep(1)

        register_button = self.driver.find_element(By.NAME, 'register-button').click()

        time.sleep(5)


