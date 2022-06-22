import time

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestLogInPage:
    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

        chrome_driver_binary = "./drivers/chromedriver"
        ser_chrome = ChromeService(chrome_driver_binary)
        self.driver = webdriver.Chrome(service=ser_chrome, options=options)

    def teardown_method(self):
        self.driver.close()


    def test_Positive_LogIn(self):
        self.driver.get('https://www.nike.com/')
        # self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys("student")
        self.driver.find_element(By.CSS_SELECTOR, '#hf_title_signin_membership').click()
        self.driver.find_element(By.CSS_SELECTOR, '#/36 8403254-c350-492d-988a-6e535738a852').click()
        self.driver.find_element(By.CSS_SELECTOR, '#/36 194db70-8a71-483b-ae98-7b071804ecf0').send_keys("amalal@ac.sce.ac.il")
        self.driver.find_element(By.CSS_SELECTOR, '#/33 e6118ee-beb4-4749-85ab-ae0bf8bac90c').send_keys("amal1996*")
        self.driver.find_element(By.CSS_SELECTOR, '#/31 501406b-ac5c-48c4-887a-bae0b19c8628').send_keys("Amal")
        self.driver.find_element(By.CSS_SELECTOR, '#/33 d8a93a6-435c-4c9d-9a19-51613d41b14c').send_keys("Saleh")
        self.driver.find_element(By.CSS_SELECTOR, '#/34 bcb10ea-9e68-4a91-8f74-0edd501f4e98').send_keys("28/05/1996")
        self.driver.find_element(By.CSS_SELECTOR, '#e02a3009-d417-4851-af8f-ca762b21fb37').click()
        self.driver.find_element(By.CSS_SELECTOR, '#ecf60123-9621-4247-8cfc-cee9c3ed9f05 > input[type=button]').click()
        self.driver.find_element(By.CSS_SELECTOR, '#eb64d318-e48f-4f48-a2ef-2191164cd94f').click()


