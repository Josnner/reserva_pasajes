from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class ReservationPage:
    def __init__(self, driver):
        self.driver = driver
        # Localizadores
        self.roundtrip_radio = (By.XPATH, "//input[@name='tripType' and @value='roundtrip']")
        self.pass_dd = (By.NAME, "passCount")
        self.depa_dd = (By.NAME, "fromPort")
        self.on_dd = (By.NAME, "fromMonth")
        self.day_dd = (By.NAME, "fromDay")
        self.arr_dd = (By.NAME, "toPort")
        self.retur_dd = (By.NAME, "toMonth")
        self.day_retur_dd = (By.NAME, "toDay")
        self.first_radio = (By.XPATH, "//input[@name='servClass' and @value='First']")
        self.airline_dd = (By.NAME, "airline")
        self.find_flights_btn = (By.NAME, "findFlights")
        self.home_button = (By.XPATH, "//img[@src='images/home.gif']")

    def select_trip_type(self):
        roundtrip_radio = self.driver.find_element(*self.roundtrip_radio)
        if not roundtrip_radio.is_selected():
            roundtrip_radio.click()

    def select_passenger_count(self, count):
        self._select_dropdown(self.pass_dd, count)

    def select_departure(self, city, month, day):
        self._select_dropdown(self.depa_dd, city)
        self._select_dropdown(self.on_dd, month)
        self._select_dropdown(self.day_dd, day)

    def select_arrival(self, city, month, day):
        self._select_dropdown(self.arr_dd, city)
        self._select_dropdown(self.retur_dd, month)
        self._select_dropdown(self.day_retur_dd, day)

    def select_class_and_airline(self, airline):
        first_radio = self.driver.find_element(*self.first_radio)
        if not first_radio.is_selected():
            first_radio.click()
        airline_dd = Select(self.driver.find_element(*self.airline_dd))
        airline_dd.select_by_visible_text(airline)
        

    def submit_reservation(self):
        self.driver.find_element(*self.find_flights_btn).click()

    def verify_home_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.home_button)
        )
        home_button = self.driver.find_element(*self.home_button)
        assert home_button.is_displayed() and home_button.is_enabled(), "El botón 'Home' no está disponible."
        home_button.click()

    def _select_dropdown(self, locator, value):
        select_element = Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)))
        select_element.select_by_value(value)

    def print_airline_options(self):
        select_element = Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.airline_dd)))
        options = select_element.options
        print("Opciones disponibles en el menú desplegable de aerolíneas:")
        for option in options:
            print(option.text)

