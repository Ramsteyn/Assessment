import pytest

from assessment.TestAssessment.Utilities.BaseClass import baseClass
from assessment.TestAssessment.Utilities.ListFunctions import GettingPositiveNewUserCredentials, GettingBadCredentials
from assessment.TestAssessment.Utilities.LoginPageElements import LoginPageElements

"""
                 Verfiy that User is able to Sign IN and Logout without issue
                                                                                          """



val = "../ConfigFiles/NewAccountCredentials.cfg"
username, firstname, lastname, password = GettingPositiveNewUserCredentials(val)
password1 = GettingBadCredentials(val)

class TestLogin(baseClass):

    @pytest.mark.smoke
    def test_loginbadcred(self, setup, credentials):
        # Initialing Log files to generate during the TC execution
        log = self.getLogger()


        # Logining in with Bad Credentials
        log.info("Before Clicking the New User registration Button")
        loginPage = LoginPageElements(self.driver)
        loginPage.UserName(credentials[1])
        loginPage.Password(credentials[0])
        loginPage.Remember(log)
        title = loginPage.SignInButton()
        assert "Cypress Real World App" == title, f"User is able to login with Bad Credentials"





    @pytest.fixture(params=[(password1, username)])
    def credentials(self, request):

        return request.param
















