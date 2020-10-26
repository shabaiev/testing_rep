import time
import pytest


@pytest.mark.parametrize("url, expected_title", [
    ("https://www.youtube.com/", "YouTube"),
    ("https://www.tesla.com/models", "Model S | Tesla"),
    ("https://www.apple.com/", "Apple"),
    ("https://www.spacex.com/", "SpaceX"),
    ("https://en.wikipedia.org/wiki/Robin_Hood", "Robin Hood - Wikipedia")])
def test_initial(browser, url, expected_title):
    browser.get(url)
    assert browser.title == expected_title
