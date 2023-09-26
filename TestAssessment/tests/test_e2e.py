import time

import pytest

from assessment.TestAssessment.Utilities.BaseClass import baseClass
from assessment.TestAssessment.Utilities.CreateTrasactionPage import CreateTransaction
from assessment.TestAssessment.Utilities.HomePageElements import HomePage
from assessment.TestAssessment.Utilities.ListFunctions import GettingCredentialsForE2E, GettingBankAccountDetails, \
    GettingAmountToSend
from assessment.TestAssessment.Utilities.LoginPageElements import LoginPageElements
from assessment.TestAssessment.Utilities.MyAccountPage import MyAccountPage
from assessment.TestAssessment.Utilities.NewAccountsPageElements import NewAccountsPageElements

"""
                 Verify that first time login in and account adding
                                                                                          """



val = "../ConfigFiles/NewAccountCredentials.cfg"
username, firstname, lastname, password = GettingCredentialsForE2E(val)

val1 = "../ConfigFiles/BankAccountDetails.cfg"
bankName, routingNumb, accountNumb = GettingBankAccountDetails(val1)

val2 = "../ConfigFiles/BankAccountDetails.cfg"
amount = GettingAmountToSend(val2)

class TestLogin(baseClass):

    @pytest.mark.E2E
    @pytest.mark.parametrize("firstname", "lastname", "password", "username", "bankName", "routingNumb", "accountNumb","amount", [
        ('Ram', 'Mani', 'Testing123', 'Ramsteyn', 'SBI', '12345678', '1234567', '$100'),
        ('Ram', 'Mani', 'Testing123', 'Ramsteyn', 'SBI', '12345678', '1234567', '$100')
                             ])
    def test_e2e(self, setup, credentials):
        # Initialing Log files to generate during the TC execution
        log = self.getLogger()

        # Creating New User
        log.info("Before Clicking the New User registration Button")
        loginPage = LoginPageElements(self.driver)
        loginPage.UserName(username)
        loginPage.NewUser()

        #  Entering the Credentials in the New User Registration Page
        log.info("Entering the Registration details")
        newUserPage = NewAccountsPageElements(self.driver)
        newUserPage.FirstName(credentials[0])
        newUserPage.LastName(credentials[1])
        newUserPage.UserName(credentials[3])
        newUserPage.PassWord(credentials[2])
        newUserPage.ConfirmPassWord(credentials[2])
        signUp = newUserPage.SignUp()
        assert signUp == "SIGN UP", f"Check that user has issue in Credentials text boxes"

        # Clicking on the SignUp Button
        log.info("Clicking the Sign Up Button")
        newUserPage.SignUp
        assert self.driver.title == "Cypress Real World App", f"Verify that user is landed in the Sign in page"


        # Logining in using the above created credentials
        log.info("Before Clicking the New User registration Button")
        loginPage = LoginPageElements(self.driver)
        loginPage.UserName(credentials[3])
        loginPage.Password(credentials[2])
        loginPage.Remember(log)
        title = loginPage.SignInButton()
        assert "Cypress Real World App" == title, f"Verify that there issue in Logging in Tabs"

        #Adding Account details
        log.info("Entering the Bank Account credentials")
        account = MyAccountPage(self.driver)
        account.NextBut()
        account.BankName(credentials[4])
        account.RoutingName(credentials[5])
        account.AccountName(credentials[6])

        # Clicking on the Done button and next button
        log.info("Clicking on the Done button and next button")
        account.SaveButton()
        account.DoneBut()


        # Verifying that added bank account is correct
        log.info("Verifying that added account is reflected in the Bank Accounts page")
        bank = HomePage(self.driver, credentials[4])
        bankName1 = bank.BankAccounts()
        assert bankName1 == credentials[4], f"Bank account is not added in the Bank accounts details page"

        # Creating a New Transaction
        log.info("Sending amount to the contact")
        transact = CreateTransaction(self.driver, credentials[7])
        transact.CreateTransaction()
        transact.ContactSearch()
        transact.ContactSelect()

        transact.AmountToSend()
        transact.AddtionalNotes()
        transact.PayButton()


        # Verifying the Amount sent is reflected in the Mine section
        bank.HomeButton()
        transact.MyTransaction()
        sent = transact.SentStatus()
        assert sent == credentials[7], f"Amount sent is not reflected in the Mine section"



    # Sending  required Testdata's for the Testcase
    @pytest.fixture(params=[(firstname, lastname, password, username, bankName, routingNumb, accountNumb,amount)])
    def credentials(self, request):
        return request.param