from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        #Localizadores
        self.firstName = (By.NAME, "firstName")
        self.lastName = (By.NAME, "lastName")
        self.phone = (By.NAME, "phone")
        self.email = (By.ID, "userName")
        self.addres = (By.NAME, "address1")
        self.city = (By.NAME, "city")
        self.state = (By.NAME, "state")
        self.code = (By.NAME, "postalCode")
        self.country = (By.NAME, "country")
        self.userName = (By.ID, "email")
        self.passWord = (By.NAME, "password")
        self.confirmPassword = (By.NAME, "confirmPassword")
        self.btn_submit = (By.NAME, "submit")

    def fill_contact_information(self, first_name, last_name, phone, email):
        self._input_text(self.firstName, first_name)
        self._input_text(self.lastName, last_name)
        self._input_text(self.phone, phone)
        self._input_text(self.email, email)
    
    def fill_mailing_information(self, addres, city, state, code, country):
        self._input_text(self.addres, addres)
        self._input_text(self.city, city)
        self._input_text(self.state, state)
        self._input_text(self.code, code)
        self._select_dropdown(self.country, country)
    
    def fill_user_information(self, username, password, confirm_passwrod):
        self._input_text(self.userName, username)
        self._input_text(self.passWord, password)
        self._input_text(self.confirmPassword, confirm_passwrod)        
    
    def submit_form(self):
        self._click_element(self.btn_submit)
    
    # Métodos privados para reutilizar en la clase
    def _input_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def _click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def _select_dropdown(self, locator, value):
        select_element = Select(self.wait.until(EC.visibility_of_element_located(locator)))
        select_element.select_by_value(value)


