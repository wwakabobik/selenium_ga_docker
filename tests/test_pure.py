"""
from os import environ
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_service = Service(environ['CHROMEWEBDRIVER'])
chrome_options = Options()
for option in ['--headless','--disable-gpu','--window-size=1920,1200','--ignore-certificate-errors','--disable-extensions','--no-sandbox','--disable-dev-shm-usage']:
    chrome_options.add_argument(option)
driver = webdriver.Chrome(service = chrome_service,options = chrome_options)
"""
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_basic():
    options = ChromeOptions()
    driver = webdriver.Remote(options=options, command_executor="http://selenium:4444")
    driver.get("https://selenium.dev")
    driver.find_element(By.XPATH, "//*[@class='card-body']/h4[.='Selenium WebDriver']")
    driver.quit()  # test
