from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Library import Element_locator_reader
from Library import Registration_login_data_reader

class Registration:
    def user_enter_username(self,driver):
        driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_registration("Username_locator")).send_keys(Registration_login_data_reader.read_registration_login_data_from_registration_login_data_cfg_file("User_name"))

    def user_enter_email(self,driver):
        driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_registration("Email_locator")).send_keys(Registration_login_data_reader.read_registration_login_data_from_registration_login_data_cfg_file("Email"))

    def user_enter_password(self,driver):
        driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_registration("Password_locator")).send_keys(Registration_login_data_reader.read_registration_login_data_from_registration_login_data_cfg_file("Password"))

    def user_enter_confirm_password(self,driver):
        driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_registration("Confirm_password_locator")).send_keys(Registration_login_data_reader.read_registration_login_data_from_registration_login_data_cfg_file("Password"))

    def user_enter_DOB(self,driver):
        driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_registration("date_of_birth_locator")).send_keys(Registration_login_data_reader.read_registration_login_data_from_registration_login_data_cfg_file("DOB"))

    def user_enter_phone(self,driver):
        driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_registration("Phone_locator")).send_keys(Registration_login_data_reader.read_registration_login_data_from_registration_login_data_cfg_file("Phone_no"))

    def user_enter_address(self,driver):
        driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_registration("Address_locator")).send_keys(Registration_login_data_reader.read_registration_login_data_from_registration_login_data_cfg_file("Address"))

    def user_enter_address_type(self,driver):
        driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_registration("Address_type_locator")).click()

    def user_select_gender(self,driver):
        gender = Select(driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_registration("Gender_locator")))
        gender.select_by_index(1)

    def user_select_country(self,driver):
        country = Select(driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_registration("Country_locator")))
        country.select_by_visible_text("India")

    def user_select_state(self,driver):
        state = Select(driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_registration("State_locator")))
        state.select_by_value("5")

    def user_select_city(self,driver):
        city = Select(driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_registration("City_locator")))
        city.select_by_visible_text("Bhabua")

    def user_enter_ZIP_code(self,driver):
        driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_registration("Zip_code_locator")).send_keys(Registration_login_data_reader.read_registration_login_data_from_registration_login_data_cfg_file("Zip_code"))

    def user_check_check_box(self,driver):
        driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_registration("Check_box_locator")).click()

    def user_click_on_read_details(self,driver):
        driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_registration("Read_details_locator")).click()

    def user_click_on_signup(self,driver):
        driver.find_element(By.XPATH,Element_locator_reader.read_element_locator_of_registration("Signup_locator")).click()
