from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Generic.Screenshot import take_screenshot


class _visibility_of_element_located(visibility_of_element_located):
    def __init__(self,locator):
        super().__init__(locator)

    def __call__(self, driver):
        result = super().__call__(driver)        #reult -> webelemnt/False
        if isinstance(result, WebElement):
            return result.is_enabled()
        else:
            return False

def loading(driver,locator):               #checking elemnt is present in DOM or not
    wait = WebDriverWait(driver, 10)
    v = _visibility_of_element_located(locator)
    try:
        wait.until(v)
    except Exception as errmsg1:
        take_screenshot(driver)
        raise errmsg1


def title_present(driver, title):
    wait = WebDriverWait(driver, 10)
    try:
        res = wait.until(EC.title_contains(title))
    except Exception as errmsg:
        take_screenshot(driver)
        raise errmsg


def error_message(driver, message):
    e_err = "Username or Password is invalid. Please try again."
    try:
        assert e_err == message,["Element is not visible"]
    except Exception as ex:
        take_screenshot(driver)
        raise ex



