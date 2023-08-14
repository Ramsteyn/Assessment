from selenium.webdriver.common.by import By

"""   
                Elements of Bank Account  Details page
                                                                             """
class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver



    create = (By.XPATH, "//span[text()='Create']")
    bankName = (By.ID, "bankaccount-bankName-input")
    routingName = (By.ID, "bankaccount-routingNumber-input")
    accountName = (By.ID, "bankaccount-accountNumber-input")
    saveButton = (By.XPATH, "//span[text()='Save']")
    nextButton = (By.XPATH, "//span[text()='Next']")
    doneButton = (By.XPATH, "//span[text()='Done']")


    def Create(self, value):
        self.value = value
        new = self.driver.find_element(*MyAccountPage.create).send_keys(self.value)

        return new

    def BankName(self, value):
        self.value = value
        bName = self.driver.find_element(*MyAccountPage.bankName).send_keys(self.value)

        return bName

    def RoutingName(self, value):
        self.value = value
        rName = self.driver.find_element(*MyAccountPage.routingName).send_keys(self.value)

        return rName

    def AccountName(self, value):
        self.value = value
        aName = self.driver.find_element(*MyAccountPage.accountName).send_keys(self.value)

        return aName

    def SaveButton(self):
        sButton = self.driver.find_element(*MyAccountPage.saveButton).click()

        return sButton

    def NextBut(self):
        next = self.driver.find_element(*MyAccountPage.nextButton).click()

        return next

    def DoneBut(self):
        done = self.driver.find_element(*MyAccountPage.doneButton).click()

        return done

