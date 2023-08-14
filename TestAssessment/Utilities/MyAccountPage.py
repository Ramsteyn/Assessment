from selenium.webdriver.common.by import By

""" 

                             Elements of New Account Creation Page

                                                                        """
class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver

    firstName = (By.ID, "user-settings-firstName-input")
    lastName = (By.ID, "user-settings-lastName-input")
    email = (By.ID, "user-settings-email-input")
    phoneNumber= (By.ID, "user-settings-phoneNumber-input")
    saveButton = (By.XPATH, "//span[text()='Save']")
    done = (By.XPATH, "//span[text()='Done']")

    def FirstName(self, value):
        self.value = value
        fname = self.driver.find_element(*MyAccountPage.firstName).send_keys(self.value)

        return fname

    def LastName(self,value):
        self.value = value
        lname = self.driver.find_element(*MyAccountPage.lastName).send_keys(self.value)

        return lname

    def Email(self, value):
        self.value = value
        mail = self.driver.find_element(*MyAccountPage.email).send_keys(self.value)

        return mail

    def PhoneNumber(self, value):
        self.value = value
        phonrNum = self.driver.find_element(*MyAccountPage.phoneNumber).send_keys(self.value)

        return phonrNum

    def SaveButton(self):
        sButton = self.driver.find_element(*MyAccountPage.saveButton).click()

        return sButton

    def Done(self):
        done = self.driver.find_element(*MyAccountPage.done).click()

        return done