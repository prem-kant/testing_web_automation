from configparser import ConfigParser
config = ConfigParser()
config.read("C:\\Users\\sony\\PycharmProjects\\complete_registration_login_of_testing_world\\ConfigurationFiles\\Element_locators.cfg")

def read_element_locator_of_registration(key):
    return config.get("Registration",key)

def read_element_locator_of_tab_change(key):
    return config.get("Tab_change_to_login",key)

def read_element_locator_of_login(key):
    return config.get("Login",key)

