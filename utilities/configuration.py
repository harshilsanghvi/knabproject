import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


def get_username():
    return "harshil2808@gmail.com"


def get_password():
    return "Trello@123"
