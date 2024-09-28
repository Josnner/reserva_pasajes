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
    context.driver.get("https://demo.guru99.com/test/newtours/register_sucess.php")

    # Inicializar la página de registro
    context.register_page = RegisterPage(context.driver)

    @when(u'Usuario llena introduce sus datos')
    def step_llenar_datos(context):
        page = context.register_page
        page.select_Contact_Information("first_Name", "last_Name", "user_Phone", "user_Email")
        page.select_Mailing_Information("self", "user_Addres, user_City", "user_State", "user_Code", "country")
        page.select_User_Information("user_name", "user_Password", "user_passwrod_confirm")
        page.select_btn()

    @then(u'Usuario registrado')
    def step_usuario_registrado(context):
           WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located((
                By.XPATH, "//b[normalize-space()='Dear a a,']")))
    texto = context.driver.find_element(By.XPATH, "from selenium.webdriver.common.by import By").text
    comparar_texto = "Dear a a,"
    assert texto == comparar_texto,f"Expected message: {texto}, but got: {comparar_texto}"