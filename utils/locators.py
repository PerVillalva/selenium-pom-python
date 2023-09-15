from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    SUBMIT = (By.ID, 'submit')
    ERROR_MESSAGE = (By.ID, 'error')
