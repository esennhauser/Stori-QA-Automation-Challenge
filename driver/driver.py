import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


@pytest.fixture(scope="class")
def test_info(request):
    browser = request.config.option.browser
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError("Browser selected not compatible. ")

    automation_practice = "https://rahulshettyacademy.com/AutomationPractice/"

    driver.maximize_window()
    errors = []
    driver.get(automation_practice)
    driver.implicitly_wait(10)

    print("Page opened: " + str(automation_practice))

    yield driver, errors

    # Printing errors
    errors_verified = errors.copy()
    for e in errors:
        if e == "":
            errors_verified.remove(e)
        else:
            pass
    if len(errors_verified) == 0:
        print("\n\t\tTest finished with no errors. ")
    else:
        print("\n\t\t{}".format(errors_verified))

    driver.quit()
    print("\t\tTest is finished.\n")

