import pytest

from assessment.TestAssessment.Utilities.BaseClass import baseClass
from assessment.TestAssessment.Utilities.ListFunctions import GettingPositiveNewUserCredentials, \
    GettingBankAccountDetails
from assessment.TestAssessment.Utilities.LoginPageElements import LoginPageElements

"""
                 Verfiy that User is able to Sign IN and Logout without issue
                                                                                          """



val = "../ConfigFiles/NewAccountCredentials.cfg"
username, firstname, lastname, password = GettingPositiveNewUserCredentials(val)

val1 = "../ConfigFiles/BankAccountDetails.cfg"
bankName, routingNumb, accountNumb = GettingBankAccountDetails(val1)

class TestLogin(baseClass):

    @pytest.mark.sanity
    def test_loginlogout(self, setup, credentials):
        # Initialing Log files to generate during the TC execution
        log = self.getLogger()


        # Logining in a Already existing user
        log.info("Before Clicking the New User registration Button")
        loginPage = LoginPageElements(self.driver)
        loginPage.UserName(credentials[1])
        loginPage.Password(credentials[0])
        loginPage.Remember(log)
        title = loginPage.SignInButton()
        assert "Cypress Real World App" ==  title, f"Verify that there issue in Logining Tabs"

        # #Logging out Successfully
        # log.info("Entering into logging out")
        # home = HomePage(self.driver, credentials[2])
        # remember = home.LogOut()
        # #remember = loginPage.Remember(log)
        # assert remember == "Remember me", f"Verify that User is unable to logOut after SIGNING IN"

    # Sending  required Testdata's for the Testcase
    @pytest.fixture(params=[(password, username, bankName)])
    def credentials(self, request):

        return request.param
















