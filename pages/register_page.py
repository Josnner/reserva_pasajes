from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
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
        self.passWord_confirm = (By.NAME, "confirmPassword")
        self.btn_submit = (By.NAME, "submit")

    def select_Contact_Information(self,first_Name, last_Name, user_Phone, user_Email):
        firstName = self.driver.find_element(*self.firstName)
        firstName.send_keys(first_Name)
        lastName = self.driver.find_element(*self.lastName)
        lastName.send_keys(last_Name)
        phone = self.driver.find_element(*self.phone)
        phone.send_keys(user_Phone)
        email = self.driver.find_element(*self.email)
        email.send_keys(user_Email)
    
    def select_Mailing_Information(self, user_Addres, user_City, user_State, user_Code, user_country):
        addres = self.driver.find_element(*self.addres)
        addres.send_keys(user_Addres)
        city = self.driver.find_element(*self.city)
        city.send_keys(user_City)
        state = self.driver.find_element(*self.state)
        state.send_keys(user_State)
        code = self.driver.find_element(*self.code)
        code.send_keys(user_Code)
        country = Select(self.driver.find_element(*self.country))
        country.select_by_value(user_country)
    
    def select_User_Information(self, user_name, user_Password, user_passwrod_confirm):
        username = self.driver.find_element(*self.userName)
        username.send_keys(user_name)
        passWord = self.driver.find_element(*self.passWord)
        passWord.send_keys(user_Password)
        passWordConfirm = self.driver.find_element(*self.passWord_confirm)
        passWordConfirm.send_keys(user_passwrod_confirm)
        
    
    def select_btn(self):
        btn_submit = self.driver.find_element(*self.btn_submit)
        btn_submit.click()


