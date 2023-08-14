Prerequisites Before Running the Tests:

1. Download the demo site and start it in the local server by completing the necessaries mentioned (https://github.com/cypress-io/cypress-realworld-app)
2. User should install python3.10 or above and make sure the path of python install is updated in the Environment variables
3. In commandPrompt/Terminal execute the following commands to meet the requirements
    a. pip install selenium
    b. pip install pytest
    c. pip install allure-pytest

NOTE: Demo application is not stable.

Steps to Run the Tests

1. Download the Package from the public github repository
2. In CMD/Terminal cd to the tests path of downloaded package i.e.."....\TestAssessment\tests"
3. Execute the following commands to run the tests
   a. py.test -m smoke --browser_name chrome --alluredir=Reports -v -s
   b. allure generate Reports/allure-html --clean (Allure report Generation)
   c. Open the index.html file generated in the above step in any browser to see the reports

Others test execution to try
   1. py.test -m sanity --browser_name firefox --alluredir=Reports -v -s
   2. py.test -m E2E --browser_name chrome --alluredir=Reports -v -s


*** Limitations of Demo Site ***
1. Make sure to delete the Generated Reports directory everytime before executing the tests (each commands mentioned in step 3)
2. If need to run the Testcase multiple time, kindly change the values in NewAccountCredentials.cfg file since the Demo app is locally hosted



