from Pages.registration import Registration
from BaseFiles import Initiate_browser
import time

def test_registration():
    driver = Initiate_browser.test_open_browser()
    Reg = Registration()
    Reg.user_enter_username(driver)
    Reg.user_enter_email(driver)
    Reg.user_enter_password(driver)
    Reg.user_enter_confirm_password(driver)
    Reg.user_enter_DOB(driver)
    Reg.user_enter_phone(driver)
    Reg.user_enter_address(driver)
    Reg.user_enter_address_type(driver)
    Reg.user_select_gender(driver)
    Reg.user_select_country(driver)
    time.sleep(4)
    Reg.user_select_state(driver)
    time.sleep(4)
    Reg.user_select_city(driver)
    time.sleep(4)
    Reg.user_enter_ZIP_code(driver)
    Reg.user_check_check_box(driver)
    # Reg.user_click_on_read_details(driver)
    # time.sleep(5)
    Reg.user_click_on_signup(driver)
    time.sleep(10)