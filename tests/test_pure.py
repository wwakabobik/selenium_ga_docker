from time import sleep
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_basic():
    sleep(30)
    options = ChromeOptions()
    driver = webdriver.Remote(options=options, command_executor="http://chrome:4444")
    driver.get("https://selenium.dev")
    driver.find_element(By.XPATH, "//*[@class='card-body']/h4[.='Selenium WebDriver']")
    driver.quit()  # test
