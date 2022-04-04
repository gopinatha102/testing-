import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Switch_To_Facebook_Page:

    Social_Facebook_Click = "//a[contains(text(),'Facebook')]"
    Create_New_Account_Button = "//span[contains(text(),'Create New Account')]"
    First_Name_Text = "//input[@name='firstname']"
    Surename_Text = "//input[@name='lastname']"
    Mobile_No_Or_Email_Text = "//input[@name='reg_email__']"
    Re_Enter_Email_Text = "//input[@name='reg_email_confirmation__']"
    New_Password_Text = "//input[@id='password_step_input']"
    Gender_Female_Radio_Button = "//label[contains(text(),'Female')]"
    Gender_male_Radio_Button = "//label[contains(text(),'Male')]"
    Gender_Custom_Radio_Button = "//label[contains(text(),'Custom')]"
    Sign_In_Button = "//button[@name='websubmit']"
    Select_Day_filed = "//select[@id='day']"
    Select_month_filed = "//select[@id='month']"
    Select_year_filed = "//select[@id='year']"
    Watch_video = "//a[@aria-label='Watch Video']"
    Unmute = "//div[@aria-label='Unmute']"

    def __init__(self, driver):
        self.driver = driver

    def social_facebook_click(self):
        button = self.driver.find_element(by=By.XPATH, value=Switch_To_Facebook_Page.Social_Facebook_Click)
        button.click()
        current_window = self.driver.current_window_handle
        # store the all collects of open tabs(parent,chilled )
        all_handler = self.driver.window_handles
        for handle in all_handler:
            print(handle)
            if handle != current_window:
                # switch to chilled window
                self.driver.switch_to.window(handle)
                print(handle)
                # using  explicitly wait class
                self.watch_video()
                time.sleep(20)
                self.unmute_button()
                time.sleep(20)

                """
                element = self.driver.find_element(by=By.XPATH, value=Switch_To_Facebook_Page.Create_New_Account_Button)
                wait = WebDriverWait(self.driver, 20)
                wait.until(EC.element_to_be_clickable(element)).click()
              
                self.first_name_text()
                self.surename_text()
                self.mobile_no_or_email()
                time.sleep(10)
                self.re_enter_email()
                time.sleep(10)
                self.new_password()
                self.data_birth_day_selection()
                self.data_brith_month_selection()
                self.data_brith_year_selection()
                self.gender_male_radio_button()
                self.sign_in_button()
                time.sleep(30)"""

                # close the window of chilled
                self.driver.close()
        # switch to parent Window
        self.driver.switch_to.window(current_window)

    def first_name_text(self):
        return self.driver.find_element(by=By.XPATH, value=Switch_To_Facebook_Page.First_Name_Text).send_keys("Gopinatha")

    def surename_text(self):
        return self.driver.find_element(by=By.XPATH, value=Switch_To_Facebook_Page.Surename_Text).send_keys("N")

    def mobile_no_or_email(self):
        return self.driver.find_element(by=By.XPATH, value=Switch_To_Facebook_Page.Mobile_No_Or_Email_Text).send_keys(
            "Gopinatha@gmail.com")

    def new_password(self):
        return self.driver.find_element(by=By.XPATH, value=Switch_To_Facebook_Page.New_Password_Text).send_keys("1256@g")

    def gender_male_radio_button(self):
        return self.driver.find_element(by=By.XPATH, value=Switch_To_Facebook_Page.Gender_male_Radio_Button).click()

    def gender_female_radio_button(self):
        return self.driver.find_element(by=By.XPATH, value=Switch_To_Facebook_Page.Gender_Female_Radio_Button).click()

    def gender_custom_radio_button(self):
        return self.driver.find_element(by=By.XPATH, value=Switch_To_Facebook_Page.Gender_Custom_Radio_Button).click()

    def sign_in_button(self):
        return self.driver.find_element(by=By.XPATH, value=Switch_To_Facebook_Page.Sign_In_Button).click()

    def re_enter_email(self):
        return self.driver.find_element(by=By.XPATH, value=Switch_To_Facebook_Page.Re_Enter_Email_Text).send_keys(
             "Gopinatha@gmail.com")

    def data_birth_day_selection(self):
        day = self.driver.find_element(by=By.XPATH, value=Switch_To_Facebook_Page.Select_Day_filed)
        select = Select(day)
        select.select_by_visible_text("10")

    def data_brith_month_selection(self):
        month = self.driver.find_element(by=By.XPATH, value=Switch_To_Facebook_Page.Select_month_filed)
        select = Select(month)
        select.select_by_visible_text("Dec")

    def data_brith_year_selection(self):
        year = self.driver.find_element(by=By.XPATH, value=Switch_To_Facebook_Page.Select_year_filed)
        select = Select(year)
        select.select_by_visible_text("1996")

    def watch_video(self):
        return self.driver.find_element(by=By.XPATH, value=Switch_To_Facebook_Page.Watch_video).click()

    def unmute_button(self):
        return self.driver.find_element(by=By.XPATH, value=Switch_To_Facebook_Page.Unmute).click()

    def cookies_display(self):
        cookies = self.driver.get_cookies()
        print(len(cookies))
