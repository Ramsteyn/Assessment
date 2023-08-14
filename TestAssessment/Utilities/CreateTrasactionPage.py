from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from TestAssessment.Utilities.ListFunctions import *
from selenium.webdriver.support.wait import WebDriverWait

"""
                            Elements of Transaction Page
                                                                                        """
class CreateTransaction:
    def __init__(self, driver, amount):
        self.driver = driver
        self.amount= amount

    createTransaction = (By.XPATH, "//span[text()=' New']")
    contactSearch = (By.ID, "user-list-search-input")
    contactSelect = (By.XPATH, "//span[text()='Edgar Johns']")
    amountToSend = (By.ID, "amount")
    addtionalNotes = (By.ID, "transaction-create-description-input")
    pay = (By.XPATH, "//span[text()='Pay']")
    req = (By.XPATH, "//span[text()='Request']")
    myTransaction = (By.XPATH, "//span[text()='Mine']")


    def CreateTransaction(self):
        crTran = self.driver.find_element(*CreateTransaction.createTransaction).click()

        return crTran

    def ContactSearch(self):
        li = self.driver.find_element(*CreateTransaction.contactSearch).send_keys("Ed")

        return li

    def ContactSelect(self):
        cSelect = self.driver.find_element(*CreateTransaction.contactSelect).click()

        return cSelect

    def AmountToSend(self):
        amount = self.driver.find_element(*CreateTransaction.amountToSend).send_keys(self.amount)

        return amount

    def AddtionalNotes(self):
        notes = self.driver.find_element(*CreateTransaction.addtionalNotes).send_keys("Be Happy")

        return notes

    def PayButton(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.element_to_be_clickable((CreateTransaction.pay)))
        notes = self.driver.find_element(*CreateTransaction.pay).click()

        return notes


    def MyTransaction(self):
        mine = self.driver.find_element(*CreateTransaction.myTransaction).click()

        return mine

    def SentStatus(self):
        status = self.driver.find_element(By.XPATH, "//span[text()='$"+str(self.amount)+".00']")
        sent = status.text
        trunc = Truncating(sent)


        return trunc