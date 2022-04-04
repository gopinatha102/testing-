import time

import pytest

from POM.Home__Page import Home_page
from POM.Shoping_page import Shoping_Process
from utilities.BaseClass import Baseclass


class Test_case_15(Baseclass):

    @pytest.mark.sanity
    def test_shoping_process(self):
        self.Login_setup()
        add_chart = Home_page(self.driver)
        lis = add_chart.Add_cart_list()
        for i in lis:
            i.click()
        time.sleep(10)
        add_chart.list_Add_cart().click()
        time.sleep(10)
        shoping = Shoping_Process(self.driver)
        total = shoping.price_total()
        time.sleep(10)
        shoping.checkout_button().click()
        shoping.first_name().send_keys("gopi")
        shoping.last_name().send_keys("n")
        shoping.postal_code().send_keys("x")
        shoping.continute_button().click()
        actual_amount=shoping.actual_total_amount()
        shoping.finish_button().click()
        text = shoping.text_completed().text
        shoping.back_to_home_page()
        time.sleep(10)
        shoping.log_out_button()
        time.sleep(10)
        assert actual_amount == str(total)
        #assert text.title() == ("Checkout: Complete!")










