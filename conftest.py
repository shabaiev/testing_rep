import pytest
import requests
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")


@pytest.fixture(scope="session", params=["chrome", "firefox", "opera", "safari"])
def browser(request):
    driver_path = "/Users/Ilya/Documents/drivers"
    browser = request.param
    if browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{driver_path}/geckodriver")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=f"{driver_path}/operadriver")
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome()
    request.addfinalizer(driver.close)
    driver.maximize_window()
    return driver



