# Import necessary modules and classes:
# - Import elements from the LoginPageLocators module.
# - Import WebDriverWait and expected_conditions from Selenium for waiting.
from utils.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define a class named LoginPage.
class LoginPage(object):
    def __init__(self, driver):
        # Initialize the LoginPage instance with a WebDriver object and locators.
        self.driver = driver
        self.locator = LoginPageLocators
        
    # Define a function to wait for the presence of an element on the page.
    def wait_for_element(self, element):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(element)
        )

    # Define a function to enter a username into the corresponding input field.
    def enter_username(self, username):
        # Wait for the presence of the username input element.
        self.wait_for_element(self.locator.USERNAME)
        # Find the username input element and send the username string to it.
        self.driver.find_element(*self.locator.USERNAME).send_keys(username)

    # Define a function to enter a password into the corresponding input field.
    def enter_password(self, password):
        # Wait for the presence of the password input element.
        self.wait_for_element(self.locator.PASSWORD)
        # Find the password input element and send the password string to it.
        self.driver.find_element(*self.locator.PASSWORD).send_keys(password)

    # Define a function to click the login button.
    def click_login_button(self):
        # Wait for the presence of the login button element.
        self.wait_for_element(self.locator.SUBMIT)
        # Find the login button element and click it.
        self.driver.find_element(*self.locator.SUBMIT).click()

    # Define a function to perform a complete login by entering username and password.
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    # Define a function to perform a login with valid user credentials.
    def login_with_valid_user(self):
        self.login("student", "Password123")
        # Return a new instance of LoginPage after the login action.
        return LoginPage(self.driver)

    # Define a function to perform a login with an invalid username and return the error message.
    def login_with_invalid_username(self):
        self.login("student23", "Password123")
        # Wait for the presence of the error message element.
        self.wait_for_element(self.locator.ERROR_MESSAGE)
        # Return the text content of the error message element.
        return self.driver.find_element(*self.locator.ERROR_MESSAGE).text
    
    # Define a function to perform a login with an invalid password and return the error message.
    def login_with_invalid_password(self):
        self.login("student", "Password12345")
        # Wait for the presence of the error message element.
        self.wait_for_element(self.locator.ERROR_MESSAGE)
        # Return the text content of the error message element.
        return self.driver.find_element(*self.locator.ERROR_MESSAGE).text
