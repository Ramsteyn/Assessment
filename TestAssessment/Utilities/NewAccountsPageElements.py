from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class NewAccountsPageElements:
    def __init__(self, driver):
        self.driver = driver

    firstName = (By.ID, "firstName")
    lastName = (By.ID, "lastName")
    userName = (By.ID, "username")
    passWord = (By.ID, "password")
    confirmPassWord = (By.ID, "confirmPassword")
    signUp = (By.XPATH, "//span[text()='Sign Up']")

    def FirstName(self, value):
        self.value = value
        fname = self.driver.find_element(*NewAccountsPageElements.firstName).send_keys(value)
        return fname

    def LastName(self, value):
        self.value = value
        lname = self.driver.find_element(*NewAccountsPageElements.lastName).send_keys(value)

        return lname

    def UserName(self, value):
        self.value = value
        uname = self.driver.find_element(*NewAccountsPageElements.userName).send_keys(self.value)

        return uname

    def PassWord(self, value):
        self.value = value
        pword = self.driver.find_element(*NewAccountsPageElements.passWord).send_keys(self.value)

        return pword

    def ConfirmPassWord(self, value):
        self.value = value
        cpword = self.driver.find_element(*NewAccountsPageElements.confirmPassWord).send_keys(self.value)


        return cpword

    def SignUp(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.presence_of_element_located(NewAccountsPageElements.signUp))
        text = self.driver.find_element(*NewAccountsPageElements.signUp).text
        self.driver.find_element(*NewAccountsPageElements.signUp).click()

        return  text

    def SignUpNeg(self, log):
        self.log = log
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.presence_of_element_located(NewAccountsPageElements.signUp))
        try:
            self.driver.find_element(*NewAccountsPageElements.signUp).click()
        except Exception as EC:
            self.log.info(EC)
            sigUp = str(EC)

        return sigUp

