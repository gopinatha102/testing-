import logging
import inspect
import pytest

from POM.Log_in_Saucedemo import Login


@pytest.mark.usefixtures("setup")
class Baseclass:

    def getLogger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        path = "C:\\Users\\DELL\\PycharmProjects\\Saucedemo\\Log Files\\logfile.log"

        filehandler = logging.FileHandler(path)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)

        logger.setLevel(logging.INFO)

        return logger

    def Login_setup(self):
        login = Login(self.driver)
        login.log_in_name().send_keys("standard_user")
        login.log_in_password().send_keys("secret_sauce")
        login.log_in_button().click()
        return login
