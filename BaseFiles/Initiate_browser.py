from selenium.webdriver import Chrome
from Library import Registration_login_data_reader

def test_open_browser():
    driver = Chrome()
    driver.maximize_window()
    driver.get(Registration_login_data_reader.read_application_data_from_registration_login_data_cfg_file("Application_URL"))
    return driver
