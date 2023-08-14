from selenium.webdriver.common.by import By





"""
                Elements of HomePage of the Payment Site 
                                                                     """




class HomePage:


    def __init__(self, driver, bankName):
        self.driver = driver
        self.bank = bankName


    homeButton = (By.XPATH, "//span[text()='Home']")
    myAccount = (By.XPATH, "//span[text()='My Account']")
    bankAccounts = (By.XPATH, "//span[text()='Bank Accounts']")
    notifications = (By.XPATH, "//span[text()='Notifications']")
    logOut = (By.XPATH, "//span[text()='Logout']")
    remember = (By.XPATH, "//span[text()='Remember me']")
    #bankName = (By.XPATH, "//p[text()="+ str(bank) +"]")

    def HomeButton(self):
         hButton = self.driver.find_element(*HomePage.homeButton).click()

         return hButton

    def MyAccountC(self):
        mButton = self.driver.find_element(*HomePage.myAccount).click()

        return mButton

    def Notifications(self):
        nButton = self.driver.find_element(*HomePage.notifications).click()

        return nButton

    def LogOut(self):
        self.driver.find_element(*HomePage.logOut).click()
        logOut = self.driver.find_element(*HomePage.remember)


        return logOut.text

    def BankAccounts(self):
        self.driver.find_element(*HomePage.bankAccounts).click()
        bButton = self.driver.find_element(By.XPATH, "//p[text()='"+str(self.bank)+"']")

        return bButton.text

