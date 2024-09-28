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
        pass_dd = Select(self.driver.find_element(*self.pass_dd))
        pass_dd.select_by_visible_text(count)

    def select_departure(self, city, month, day):
        depa_dd = Select(self.driver.find_element(*self.depa_dd))
        depa_dd.select_by_value(city)
        on_dd = Select(self.driver.find_element(*self.on_dd))
        day_dd = Select(self.driver.find_element(*self.day_dd))
        on_dd.select_by_value(month)
        day_dd.select_by_value(day)

    def select_arrival(self, city, month, day):
        arr_dd = Select(self.driver.find_element(*self.arr_dd))
        retur_dd = Select(self.driver.find_element(*self.retur_dd))
        day_retur_dd = Select(self.driver.find_element(*self.day_retur_dd))
        arr_dd.select_by_value(city)
        retur_dd.select_by_value(month)
        day_retur_dd.select_by_value(day)

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

