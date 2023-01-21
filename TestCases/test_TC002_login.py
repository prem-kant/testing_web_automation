from BaseFiles import Initiate_browser
from Pages.Login import login
import time

def test_login():
    driver = Initiate_browser.test_open_browser()
    login1 = login()
    login1.tab_change(driver)
    login1.enter_username_for_login(driver)
    login1.enter_password_for_login(driver)
    login1.click_on_ClickOnLogin(driver)
    login1.click_on_login(driver)
    time.sleep(20)
