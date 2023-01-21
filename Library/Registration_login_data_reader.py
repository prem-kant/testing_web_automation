from configparser import ConfigParser
config = ConfigParser()
config.read("C:\\Users\\sony\\PycharmProjects\\complete_registration_login_of_testing_world\\ConfigurationFiles\\Registration_login_data.cfg")

def read_application_data_from_registration_login_data_cfg_file(key):
    return config.get("Application",key)

def read_registration_login_data_from_registration_login_data_cfg_file(key):
    return config.get("Registration_login",key)