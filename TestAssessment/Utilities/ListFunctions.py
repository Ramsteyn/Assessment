import configparser


"""  
                                        List of Function page used in the test cases

                                                                                                                      """
#Parsing the cfg file for TestData's
def GettingtheCredentials( value):
    config = configparser.ConfigParser()
    config.read(value)
    return config


#Used for checking the amount sent
def Truncating( value):
    li = value[2:5]
    return li

#Used for getting Positive user credentials during account sign up
def GettingPositiveNewUserCredentials(value):
    userName = GettingtheCredentials(value)["PostiveAndLoginCredentials"]["UserName"]
    firstName = GettingtheCredentials(value)["PostiveAndLoginCredentials"]["FirstName"]
    lastName = GettingtheCredentials(value)["PostiveAndLoginCredentials"]["LastName"]
    password = GettingtheCredentials(value)["PostiveAndLoginCredentials"]["Password"]

    return userName, firstName, lastName , password


#Used for getting Negative user credentials during account sign up
def GettingNegativeNewUserCredentials(value):
    userName = GettingtheCredentials(value)["NegativeCredentials"]["UserName"]
    firstName = GettingtheCredentials(value)["NegativeCredentials"]["FirstName"]
    lastName = GettingtheCredentials(value)["NegativeCredentials"]["LastName"]
    password = GettingtheCredentials(value)["NegativeCredentials"]["Password"]

    return userName, firstName, lastName , password

# Used for getting Negative Login Credentials
def GettingBadCredentials(value):
    password = GettingtheCredentials(value)["WrongPassword"]["Password"]

    return  password

# Used for Getting Bank Account details
def GettingBankAccountDetails(value):
    bankName = GettingtheCredentials(value)["PositiveAccountDetails"]["BankName"]
    routingNumb = GettingtheCredentials(value)["PositiveAccountDetails"]["RoutingNumber"]
    accountNumb = GettingtheCredentials(value)["PositiveAccountDetails"]["AccountNumber"]


    return bankName, routingNumb, accountNumb

# Used for getting in the Amount to send
def GettingAmountToSend(value):
    amount = GettingtheCredentials(value)["AmountToBeSent"]["Amount"]

    return amount

# E2E TestData
def GettingCredentialsForE2E(value):
    userName = GettingtheCredentials(value)["E2ECredentials"]["UserName"]
    firstName = GettingtheCredentials(value)["E2ECredentials"]["FirstName"]
    lastName = GettingtheCredentials(value)["E2ECredentials"]["LastName"]
    password = GettingtheCredentials(value)["E2ECredentials"]["Password"]

    return userName, firstName, lastName , password