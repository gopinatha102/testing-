import time
import pytest
import allure
import sys
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from POM.Home__Page import Home_page
from POM.Log_in_Saucedemo import Login
from Test_Data.Home_Page_Data import Home_Page_Data
from utilities.BaseClass import Baseclass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
sys.path.append("C:\\Users\\DELL\\PycharmProjects\\Saucedemo")


@allure.severity(allure.severity_level.NORMAL)
class Test_case_0007(Baseclass):

    @pytest.mark.sanity
    @pytest.mark.skip
    @allure.severity(allure.severity_level.MINOR)
    def test_login_page(self, getData):
        log_file = self.getLogger()
        log_file.info("Login Page Start")
        self.driver.implicitly_wait(10)
        login = Login(self.driver)
        login.log_in_name().clear()
        login.log_in_name().send_keys(getData["user_name"])
        login.log_in_password().clear()
        login.log_in_password().send_keys(getData["password"])
        login.log_in_button().click()

        current_url_txt = self.driver.current_url

        if current_url_txt == "https://www.saucedemo.com/inventory.html":
            print(current_url_txt)
            log_file.info("Login Test Case 1 Executed Successfully ")
            assert True
        else:
            act_text = login.log_in_error().text
            if act_text == "Epic sadface: Username is required":
                print(act_text)
                log_file.info(act_text)
                log_file.info("Login Test Case 1 Executed Successfully ")
                assert True
            elif act_text == "Epic sadface: Password is required":
                print(act_text)
                log_file.info(act_text)
                log_file.info("Login Test Case 2 Executed Successfully ")
                assert True

            elif act_text == "Epic sadface: Username is required":
                print(act_text)
                log_file.info(act_text)
                log_file.info("Login Test Case 3 Executed Successfully ")
                assert True

            elif act_text == "Epic sadface: Username and password do not match any user in this service":
                print(act_text)
                log_file.info(act_text)
                log_file.info("Login Test Case 3 Executed Successfully ")
                self.driver.save_screenshot("image1.png")
                assert True

            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_login_page",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot("image.png")
            self.driver.refresh()

    @pytest.mark.sanity
    @step("Login correct password and user Name Display Home Page  ")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_case_home_page(self):
        log_file = self.getLogger()
        self.driver.implicitly_wait(10)
        log_file.info("Home Page is Login Started ")
        # log = Login(self.driver)
        self.Login_setup()
        # log.Login_setup()
        """login=Login(self.driver)
        login.log_in_name().send_keys("standard_user")
        login.log_in_password().send_keys("secret_sauce")
        login.log_in_button().click()"""
        home_page = Home_page(self.driver)
        home_page.open_menu_click().click()
        home_page.All_items_click().click()
        time.sleep(10)
        #home_page.scroll_specific_element()
        home_page.Switch_to_Window()
        time.sleep(20)
        self.driver.implicitly_wait(20)
        Total_list = home_page.Add_cart_list()

        count = 0
        for items in Total_list:
            items.click()
            count += 1
        print(count)
        assert count > 5

    @pytest.mark.xfail
    @step("Login correct password and user Name Display List Count Cart  ")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_Cart_list(self):
        self.driver.implicitly_wait(10)
        # log = Login(self.driver)
        # log.Login_setup()
        log_file = self.getLogger()
        log_file.info("Test Cart List is Started")
        self.Login_setup()

        Cart_list = Home_page(self.driver)
        time.sleep(10)
        Add = Cart_list.Add_cart_list()

        for Add_items in Add:
            Add_items.click()

        Cart_list.list_Add_cart().click()
        time.sleep(10)
        Cart_list.remove_list_cart().click()
        time.sleep(10)
        total_cart_list = Cart_list.total_cart_list()
        count = 0

        for items in total_cart_list:
            count += 1
        count = count + 1
        print(count)
        assert count > 6

    @pytest.mark.skip
    @step("Login correct password and user Name Display List Count Cart  ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_total_no_items(self):
        # log = Login(self.driver)
        # log.Login_setup()

        self.Login_setup()
        log_file = self.getLogger()
        log_file.info("Test Total Number of Items is Started")
        total_no = Login(self.driver)
        total = total_no.total_items_no()
        count = 0
        L = []
        for items in total:
            L.append(items.text)
            count += 1
        print(L)
        assert count >= 5

    # @pytest.fixture(params=Home_Page_Data.getTestData("Testcase4"))
    @pytest.fixture(params=Home_Page_Data.Home_Page_Data)
    def getData(self, request):
        return request.param
