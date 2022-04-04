import time

from utilities.BaseClass import Baseclass
from POM.Switch_to_facebook import Switch_To_Facebook_Page


class Test_case_100(Baseclass):

    def test_switch_to_facebook_page(self):
        print("Switch to Facebook Page is Started ")
        self.Login_setup()
        facebook_page = Switch_To_Facebook_Page(self.driver)
        time.sleep(10)
        facebook_page.social_facebook_click()
        time.sleep(10)
        facebook_page.cookies_display()
        """
        facebook_page.first_name_text()
        facebook_page.surename_text()
        facebook_page.mobile_no_or_email()
        facebook_page.new_password()
        facebook_page.gender_male_radio_button()
        facebook_page.sign_in_button()
        """




