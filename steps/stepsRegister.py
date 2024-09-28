from behave import given, when, then
from selenium.webdriver.chrome.service import Service
from pages.register_page import RegisterPage
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@given(u'Usuario navega en la pagina')
def step_open_browser(context):
    # Especificar la ruta de tu chromedriver local
    chrome_driver_path = r"D:\Testing\chromedriver\chromedriver.exe"

    # Inicializar el servicio con el ChromeDriver
    service = Service(chrome_driver_path)
    context.driver = webdriver.Chrome(service=service)

    # Navegar a la página especificada
    context.driver.get("https://demo.guru99.com/test/newtours/register.php")

    # Inicializar la página de registro
    context.register_page = RegisterPage(context.driver)

@when(u'Usuario llena introduce sus datos')
def step_llenar_datos(context):
        page = context.register_page
        page.select_Contact_Information("John", "Doe", "1234567890", "johndoe@example.com")
        page.select_Mailing_Information("123 Main St", "New York", "NY", "10001", "AUSTRALIA")
        page.select_User_Information("johndoe", "password123", "password123")
        page.select_btn()

@then(u'Usuario registrado')
def step_usuario_registrado(context):
      # Esperar a que aparezca el mensaje de confirmación
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//b[contains(text(), 'Dear')]")))
    texto = context.driver.find_element(By.XPATH, "//b[contains(text(), 'Dear')]").text
    comparar_texto = "Dear John Doe,"
    assert texto == comparar_texto, f"Expected message: {comparar_texto}, but got: {texto}"