from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'Open browser')
def step_open_browser(context):
     # Especificar la ruta de tu chromedriver local
    chrome_driver_path = r"D:\Testing\chromedriver\chromedriver.exe"  # Cambia esta ruta a la ubicación correcta de tu chromedriver

    # Inicializar el servicio con el ChromeDriver
    service = Service(chrome_driver_path)

    # Inicializar el navegador Chrome con el servicio
    context.driver = webdriver.Chrome(service=service)

    # Navegar a la página especificada
    context.driver.get("https://demo.guru99.com/test/newtours/")

@when(u'Ingresa username "{username}" y password "{password}"')
def step_username_password(context,username,password):
    context.driver.find_element(By.NAME, "userName").send_keys(username)
    context.driver.find_element(By.NAME, "password").send_keys(password)
    
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.NAME, "submit")))
    context.driver.find_element(By.NAME,"submit").click()    


@then(u'Inicio exitoso')
def step_Login(context):
    WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "font[face='Arial, Helvetica, sans-serif'] b")))
    welcome = context.driver.find_element(By.CSS_SELECTOR, "font[face='Arial, Helvetica, sans-serif'] b").text
    texto = "Thank you for Loggin."
    assert welcome == texto, f"Error: El texto esperado era '{texto}', pero se obtuvo '{welcome}'"