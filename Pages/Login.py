from selenium.webdriver.common.by import By
from Library import Element_locator_reader
from Library import Registration_login_data_reader

class login():
    def tab_change(self,driver):
        driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_tab_change("Change_tab_to_login_locator")).click()

    def enter_username_for_login(self,driver):
        driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_login("Login_username_locator")).send_keys(Registration_login_data_reader.read_registration_login_data_from_registration_login_data_cfg_file("User_name"))

    def enter_password_for_login(self,driver):
        driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_login("login_password_locator")).send_keys(Registration_login_data_reader.read_registration_login_data_from_registration_login_data_cfg_file("Password"))

    def click_on_ClickOnLogin(self,driver):
        driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_login("Keep_me_login_locator")).click()

    def click_on_login(self,driver):
        driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_login("Login_locator")).click()

