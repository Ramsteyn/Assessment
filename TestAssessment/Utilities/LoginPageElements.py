from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPageElements:
    def __init__(self, driver):
        self.driver = driver

    userName = (By.ID, "username")
    passWord = (By.ID, "password")
    signIn = (By.XPATH, "//span[text()='Sign In']")
    rememberMe = (By.NAME, "remember")
    newUser = (By.LINK_TEXT, "Don't have an account? Sign Up")

    def UserName(self, value):
        self.value = value
        self.driver.find_element(*LoginPageElements.userName).send_keys(self.value)
        return

    def Password(self, value):
        self.value = value
        pword = self.driver.find_element(*LoginPageElements.passWord).send_keys(self.value)

        return pword

    def SignInButton(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.element_to_be_clickable((LoginPageElements.signIn)))
        self.driver.find_element(*LoginPageElements.signIn).click()
        signButton = self.driver.title

        return signButton

    def Remember(self, log):
        self.log = log
        self.driver.find_element(*LoginPageElements.rememberMe).click()
        remember = self.driver.find_element(*LoginPageElements.rememberMe)
        self.log.info(remember.text)

        return remember

    def NewUser(self):
        nuser = self.driver.find_element(*LoginPageElements.newUser).click()

        return nuser
