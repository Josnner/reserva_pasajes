from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.reservation_page import ReservationPage
import time

@given(u'Open browser reserve')
def step_open_browser_reserve(context):
    # Especificar la ruta de tu chromedriver local
    chrome_driver_path = r"D:\Testing\chromedriver\chromedriver.exe"

    # Inicializar el servicio con el ChromeDriver
    service = Service(chrome_driver_path)
    context.driver = webdriver.Chrome(service=service)

    # Navegar a la página especificada
    context.driver.get("https://demo.guru99.com/test/newtours/reservation.php")
    time.sleep(2)

    # Inicializar la página de reservación
    context.reservation_page = ReservationPage(context.driver)

@when(u'Fill in the fields')
def step_fill_fields(context):
    page = context.reservation_page
    page.select_trip_type()
    page.select_passenger_count("4")
    page.select_departure("New York", "3", "1")
    page.select_arrival("Seattle", "5", "29")
    page.select_class_and_airline("Pangea Airlines")
    page.submit_reservation()

@then(u'Can flight')
def step_can_flight(context):
    context.reservation_page.verify_home_button()
    time.sleep(1)