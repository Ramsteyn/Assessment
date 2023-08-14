import pytest

from TestAssessment.Utilities.BaseClass import baseClass
from TestAssessment.Utilities.ListFunctions import GettingNegativeNewUserCredentials
from TestAssessment.Utilities.LoginPageElements import LoginPageElements
from TestAssessment.Utilities.NewAccountsPageElements import NewAccountsPageElements

"""
                    Verify user is unable to created an account with Invalid Credentials
                                                                                                              """


val = "../ConfigFiles/NewAccountCredentials.cfg"
username, firstname, lastname, password = GettingNegativeNewUserCredentials(val)

class TestLogin(baseClass):

    @pytest.mark.smoke
    def test_createnegative(self, setup, credentials):
        # Initialing Log files to generate during the TC execution
        log = self.getLogger()


        # Clickig on the New User Registration
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
        signUp = newUserPage.SignUpNeg(log)
        assert 'element click intercepted' in signUp, f"Check that user has issue in Credentials text boxes"

    # Sending  required Testdata's for the Testcase
    @pytest.fixture(params=[(firstname, lastname, password, username)])
    def credentials(self, request):

        return request.param
















