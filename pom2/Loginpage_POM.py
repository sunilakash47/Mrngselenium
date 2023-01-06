from Generic import Exclelib
from Generic.wait import *

class Login:
   locator = Exclelib.read_locator("Loginpage")

   def __init__(self, driver):
      self.driver = driver

   def username(self,data):
      loading(self.driver,Login.locator["username-txtfield"])
      self.driver.find_element(*Login.locator["username-txtfield"]).send_keys(data)

   def password(self,data):
      loading(self.driver, Login.locator["password-txtfield"])
      self.driver.find_element(*Login.locator["password-txtfield"]).send_keys(data)

   def loginbtn(self):
      loading(self.driver, Login.locator["login-btn"])
      self.driver.find_element(*Login.locator["login-btn"]).click()

   def errormsg(self):
      err = self.driver.find_element(*Login.locator["errormessage"])
      error_message(self.driver, err.text)









