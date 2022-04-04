import time

from selenium.webdriver.common.by import By


class Shoping_Process:
    checkout = "//button[@id='checkout']"
    first_name_text = "//input[@id='first-name']"
    last_name_text = "//input[@id='last-name']"
    postal_code_text = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"
    finish = "//button[@id='finish']"
    text = "//span[text()='Checkout: Complete!']"
    Back_to_Home_page_button = "//button[contains(text(),'Back Home')]"
    open_menu_button = "//button[contains(text(),'Open Menu')]"
    Log_out_button = "//a[contains(text(),'Logout')]"
    price_total_captrue = "//div[@class='inventory_item_price']"
    actual_total = "//div[@class='summary_subtotal_label']"

    def __init__(self, driver):
        self.driver = driver

    def checkout_button(self):
        return self.driver.find_element(by=By.XPATH, value=Shoping_Process.checkout)

    def first_name(self):
        return self.driver.find_element(by=By.XPATH, value=Shoping_Process.first_name_text)

    def last_name(self):
        return self.driver.find_element(by=By.XPATH, value=Shoping_Process.last_name_text)

    def postal_code(self):
        return self.driver.find_element(by=By.XPATH, value=Shoping_Process.postal_code_text)

    def continute_button(self):
        return self.driver.find_element(by=By.XPATH, value=Shoping_Process.continue_button)

    def finish_button(self):
        return self.driver.find_element(by=By.XPATH, value=Shoping_Process.finish)

    def text_completed(self):
        return self.driver.find_element(by=By.XPATH, value=Shoping_Process.text)

    def back_to_home_page(self):
        return self.driver.find_element(by=By.XPATH, value=Shoping_Process.Back_to_Home_page_button).click()

    def log_out_button(self):
        self.driver.find_element(by=By.XPATH, value=Shoping_Process.open_menu_button).click()
        time.sleep(10)
        self.driver.find_element(by=By.XPATH, value=Shoping_Process.Log_out_button).click()

    def price_total(self):
        all_price_ele = self.driver.find_elements(by=By.XPATH, value=Shoping_Process.price_total_captrue)
        total_elements = ""
        for total in all_price_ele:
            total_elements = total_elements + total.text
        l = list(total_elements.split("$"))
        l.remove("")
        total_amount = sum([float(i) for i in l])
        return total_amount

    def actual_total_amount(self):
        actual_amount = self.driver.find_element(by=By.XPATH, value=Shoping_Process.actual_total).text
        l = actual_amount.split("$")
        del l[0]
        return l[0]
