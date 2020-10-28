import pytest
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--driver_folder", default="/Users/Ilya/Documents/drivers")


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("browser")
    folder = request.config.getoption("driver_folder")

    if browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{folder}/geckodriver")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=f"{folder}/operadriver")
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

    request.addfinalizer(driver.close)
    driver.maximize_window()
    return driver
