from Generic import Exclelib
from Generic.wait import *

class Home:
    locator = Exclelib.read_locator("Homepage")

    def __init__(self, driver):
        self.driver = driver

    def userstab(self):
        loading(self.driver, Home.locator["users-tab"])
        self.driver.find_element(*Home.locator["users-tab"]).click()

    def userbtn(self):
        loading(self.driver, Home.locator["user-btn"])
        self.driver.find_element(*Home.locator["user-btn"]).click()
        try:
            cuser = self.driver.find_element(*Home.locator["Create-user-page"])
            assert cuser.text == "Create New User"
        except Exception as err:
            take_screenshot(self.driver)
            raise err

    def firstname(self,data):
        loading(self.driver, Home.locator["Firstname-txt"])
        self.driver.find_element(*Home.locator["Firstname-txt"]).send_keys(data)

    def lastname(self, data):
        loading(self.driver, Home.locator["Lastname-txt"])
        self.driver.find_element(*Home.locator["Lastname-txt"]).send_keys(data)

    def email(self, data):
        loading(self.driver, Home.locator["Email-txt"])
        self.driver.find_element(*Home.locator["Email-txt"]).send_keys(data)

    def username(self, data):
        loading(self.driver, Home.locator["Username-txt"])
        self.driver.find_element(*Home.locator["Username-txt"]).send_keys(data)

    def password(self, data):
        loading(self.driver, Home.locator["Password-txt"])
        self.driver.find_element(*Home.locator["Password-txt"]).send_keys(data)

    def retypepassword(self, data):
        loading(self.driver, Home.locator["Re-type-txt"])
        self.driver.find_element(*Home.locator["Re-type-txt"]).send_keys(data)

    def createuserbtn(self):
        loading(self.driver, Home.locator["Create-user btn"])
        self.driver.find_element(*Home.locator["Create-user btn"]).click()

    def logout(self):
        loading(self.driver, Home.locator["Logout"])
        self.driver.find_element(*Home.locator["Logout"]).click()

