import pytest
from selenium.webdriver import Chrome

@pytest.fixture
def setup():
    driver = Chrome()
    driver.get("http://localhost/login.do")
    driver.maximize_window()
    yield driver
    driver.close()

