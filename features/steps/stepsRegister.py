from behave import given, when, then
from pages.register_page import RegisterPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.driver_factory import get_chrome_driver
import logging

@given(u'Usuario navega en la pagina')
def step_open_browser(context):
    logging.info("Inicializando el navegador y navegando a la página de registro.")
    context.driver = get_chrome_driver()
    # Navegar a la página especificada
    context.driver.get("https://demo.guru99.com/test/newtours/register.php")
    # Inicializar la página de registro
    context.register_page = RegisterPage(context.driver)

@when(u'Usuario llena introduce sus datos')
def step_fill_form(context):
    logging.info("Llenando el formulario de registro con datos de usuario.")
    try:
        page = context.register_page
        page.fill_contact_information("John", "Doe", "1234567890", "johndoe@example.com")
        page.fill_mailing_information("123 Main St", "New York", "NY", "10001", "AUSTRALIA")
        page.fill_user_information("johndoe", "password123", "password123")
        page.submit_form()
        logging.info("Formulario enviado correctamente.")
    except Exception as e:
        logging.error(f"Error al llenar el formulario: {str(e)}")
        raise

@then(u'Usuario registrado')
def step_verify_registration(context):
    try:
        WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//b[contains(text(), 'Dear')]")))
        confirmation_text = context.driver.find_element(By.XPATH, "//b[contains(text(), 'Dear')]").text
        expected_text = "Dear John Doe,"
        assert confirmation_text == expected_text, f"Expected: {expected_text}, but got: {confirmation_text}"
        logging.info(f"Registro completado: {confirmation_text}")
    except Exception as e:
        # Guardar captura de pantalla en caso de error
        context.driver.save_screenshot("screenshots/error_registration.png")
        logging.error(f"Error: {str(e)}. Captura de pantalla guardada.")
        raise