import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as fs
from selenium.webdriver.firefox.options import Options as fo
import os
import platform

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action= "store", default ="chrome"
    )

def get_os_info():
    """
    Get information about the current operating system.
    Returns:
        - OS name (e.g., "Windows", "Linux", "Darwin" for macOS)
        - Binary paths for Chrome and Firefox (if available)
    """
    os_name = platform.system()

    if os_name == "Windows":
        # Binary paths for Chrome and Firefox on Windows
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    elif os_name == "Linux":
        # Binary paths for Chrome and Firefox on Linux
        chrome_path = "/usr/bin/google-chrome"
        firefox_path = "/usr/bin/firefox"
    elif os_name == "Darwin":
        # Binary paths for Chrome and Firefox on macOS
        chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        firefox_path = "/Applications/Firefox.app/Contents/MacOS/firefox"
    else:
        chrome_path = "Unknown"
        firefox_path = "Unknown"

    return os_name, chrome_path, firefox_path

# Example usage:
os_name, chrome_path, firefox_path = get_os_info()
print(os_name)

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        options = Options()
        options.add_argument('headless')
        options.add_experimental_option('detach', True)
        ser_obj = Service("../Drivers/chromedriver.exe")
        driver = webdriver.Chrome(service=ser_obj, options=options)

    elif browser == "firefox":
        opFire = fo()
        opFire.binary_location = firefox_path
        ser_objfire = fs("../Drivers/geckodriver.exe")
        driver = webdriver.Firefox(service=ser_objfire, options=opFire)

    driver.implicitly_wait(5)
    driver.get("http://www.amazon.com")
    driver.maximize_window()

        # To pass the driver
        # request.cls.driver =
    request.cls.driver = driver

    yield
    driver.close()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)


