
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Login:
    User_Name = "//input[@name='user-name']"
    Password = "//input[@id='password']"
    Login_button = "//input[@id='login-button']"
    Login_error = "//div[@class='error-message-container error']"
    # total_no_items = "//div[@class='inventory_item_price']"
    # car_total_list = "//div[@class='inventory_item_name']"
    total_no_items = "//div[@class='inventory_item_name']"
    select_list = "//select[@class='product_sort_container']"

    def __init__(self, driver):
        self.driver = driver

    def log_in_name(self):
        # return self.driver.find_element_by_xpath(Login.User_Name)
        return self.driver.find_element(by=By.XPATH, value=Login.User_Name)

    def log_in_password(self):
        # return self.driver.find_element_by_xpath(Login.Password)
        return self.driver.find_element(by=By.XPATH, value=Login.Password)

    def log_in_button(self):
        # return self.driver.find_element_by_xpath(Login.Login_button)
        return self.driver.find_element(by=By.XPATH, value=Login.Login_button)

    def log_in_error(self):
        # return self.driver.find_element_by_xpath(Login.Login_error )
        return self.driver.find_element(by=By.XPATH, value=Login.Login_error)

    def total_items_no(self):
        # total = self.driver.find_elements_by_xpath(Login.total_no_items)
        total = self.driver.find_elements(by=By.XPATH, value=Login.total_no_items)
        return total

    def select_order(self):
        # element = self.driver.find_element_by_xpath(Login.select_list)
        element = self.driver.find_element(by=By.XPATH, value=Login.select_list)
        drp = Select(element)
        ele = drp.select_by_visible_text("Name (Z to A)")
        return ele

    """def Login_setup(self):

        login = Login(self.driver)
        login.log_in_name().send_keys("standard_user")
        login.log_in_password().send_keys("secret_sauce")
        login.log_in_button().click()
        return login
"""
