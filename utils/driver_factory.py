# utils/driver_factory.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_chrome_driver():
    chrome_driver_path = r"D:\Testing\chromedriver\chromedriver.exe"
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver
