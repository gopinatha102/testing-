import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Home_page:
    open_menu = "//button[contains(text(),'Open Menu')]"
    All_items = "//a[contains(text(),'All Items')]"
    Add_cart = "//button[contains(text(),'Add to cart')]"
    cart_list = "//a[@class='shopping_cart_link']"
    remove_cart_list = "//div[text()='Sauce Labs Backpack']/../..//button[text()='Remove']"
    car_total_list = "//div[@class='cart_item']"
    social_click = "//ul[@class='social']"
    social_facebook_click = "//a[contains(text(),'Facebook')]"
    watch_video = "//div[@class='l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn " \
                  "owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 " \
                  "rq0escxv d1544ag0 tw6a2znq s1i5eluu qypqp5cg']"

    def __init__(self, driver):
        self.driver = driver

    def open_menu_click(self):
        # return self.driver.find_element_by_xpath(Home_page.open_menu)
        return self.driver.find_element(by=By.XPATH, value=Home_page.open_menu)

    def All_items_click(self):
        # return self.driver.find_element_by_xpath(Home_page.All_items)
        return self.driver.find_element(by=By.XPATH, value=Home_page.All_items)

    def Add_cart_list(self):
        # total = self.driver.find_elements_by_xpath(Home_page.Add_cart)
        total = self.driver.find_elements(by=By.XPATH, value=Home_page.Add_cart)
        return total

    def list_Add_cart(self):
        # return self.driver.find_element_by_xpath(Home_page.cart_list)
        return self.driver.find_element(by=By.XPATH, value=Home_page.cart_list)

    def remove_list_cart(self):
        # return self.driver.find_element_by_xpath(Home_page.remove_cart_list)
        return self.driver.find_element(by=By.XPATH, value=Home_page.remove_cart_list)

    def total_cart_list(self):
        # total_list = self.driver.find_elements_by_xpath(Home_page.car_total_list)
        total_list = self.driver.find_elements(by=By.XPATH, value=Home_page.car_total_list)
        return total_list

    # Scroll bar till specific Place
    def scroll_down(self):
        return self.driver.execute_script("window.scrollBy(0,1000)", " ")

    # Scroll bar till end
    def scroll_end(self):
        return self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    # Scroll bar by using specific element
    def scroll_specific_element(self):
        flag = self.driver.find_element(by=By.XPATH, value=Home_page.social_facebook_click)
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.execute_script("arguments[0].click();", flag)

    # window handler methode  are used
    def Switch_to_Window(self):
        button = self.driver.find_element(by=By.XPATH, value=Home_page.social_facebook_click)
        self.driver.execute_script("arguments[0].click();", button)
        # using find the current Window open
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
                element = self.driver.find_element(by=By.XPATH, value=Home_page.watch_video)
                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.element_to_be_clickable(element)).click()
                # close the window of chilled
                self.driver.close()
        # switch to parent Window
        self.driver.switch_to.window(current_window)


