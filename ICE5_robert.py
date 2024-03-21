# #############################################################################
# Title:          ICE5_robert
# Author:         Robert Macklem
# Date:           March 20, 2024
# Description:    Some more testing with Selenium
# #############################################################################
# Generated (in part) by Selenium IDE

#imports (deleted unused)
from selenium import webdriver
from selenium.webdriver.common.by import By

#Test class
class TestMercuryTours():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    #Get the site loaded
    self.driver.get("https://demo.guru99.com/test/newtours/")
    self.driver.set_window_size(1936, 1048)

    #Fill out login details (tutorial) + submit
    self.driver.find_element(By.NAME, "userName").click()
    self.driver.find_element(By.NAME, "userName").send_keys("tutorial")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("tutorial")
    self.driver.find_element(By.NAME, "submit").click()
    
    #Assert the login success based ont ext present
    assert self.driver.find_element(By.CSS_SELECTOR, "h3").text == "Login Successfully"
    
  def test_registration(self):
    #Get the site loaded
    self.driver.get("https://demo.guru99.com/test/newtours/")
    self.driver.set_window_size(1936, 1048)

    #Fill out registration details + submit
    self.driver.find_element(By.LINK_TEXT, "REGISTER").click()
    self.driver.find_element(By.NAME, "firstName").click()
    self.driver.find_element(By.NAME, "firstName").send_keys("Robert")
    self.driver.find_element(By.NAME, "lastName").send_keys("Macklem")
    self.driver.find_element(By.NAME, "phone").send_keys("9995551234")
    self.driver.find_element(By.ID, "userName").send_keys("fake@email.com")
    self.driver.find_element(By.NAME, "address1").send_keys("123 Fake St.")
    self.driver.find_element(By.NAME, "city").send_keys("City")
    self.driver.find_element(By.NAME, "state").send_keys("State")
    self.driver.find_element(By.NAME, "postalCode").send_keys("1J1J1J")
    self.driver.find_element(By.NAME, "country").click()
    dropdown = self.driver.find_element(By.NAME, "country")
    dropdown.find_element(By.XPATH, "//option[. = 'CANADA']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(42)").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("robert")
    self.driver.find_element(By.NAME, "password").send_keys("password1")
    self.driver.find_element(By.NAME, "confirmPassword").send_keys("password1")
    self.driver.find_element(By.NAME, "submit").click()

    #Assert registration succesful based on text present
    assert self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(2) > font").text == "Thank you for registering. You may now sign-in using the user name and password you\\\'ve just entered."

#Main  
if __name__ == "__main__":
    #Instance
    test = TestMercuryTours()

    #Setup
    test.setup_method(None)

    #Run Tests
    test.test_login()
    test.test_registration()

    #Teardown
    test.teardown_method(None)