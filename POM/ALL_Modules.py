import time

from selenium.webdriver.common.action_chains import ActionChains


class Test_All_Modules:
    all_button = "//a[@id='nav-hamburger-menu']"
    # all_button = "//header/div[@id='navbar']/div[@id='nav-main']/div[1]/a[1]/span[1]"
    echo_click = "//div[contains(text(),'Echo & Alexa')]"
    Echo_Show = "// a[contains(text(), 'Echo Show 8')]"

    def __init__(self, driver):
        self.driver = driver

    def all_button_click(self):
        self.driver.implicitly_wait(10)
        All = self.driver.find_element_by_xpath(Test_All_Modules.all_button).click()
        echo = self.driver.find_element_by_xpath(Test_All_Modules.echo_click)
        echo_show = self.driver.find_element_by_xpath(Test_All_Modules.Echo_Show)
        a = ActionChains(self.driver)
        a.move_to_element(echo).click().move_to_element(echo_show).click().perform()
        #a.double_click(All).perform()  # Double_click option
        #a.context_click(a).perform()  # Right click option
       # a.drag_and_drop().perform()  # drag and drop option
