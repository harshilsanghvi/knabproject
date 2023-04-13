from utilities.configuration import *
from helper.helper_web import get_browser


def before_feature(context, feature):
    if "uiautomation" in context.feature.tags:
        print(context.feature.tags)
        helper_func = get_browser(get_config()['ENV']['browser'])
        context.helperfunc = helper_func
        context.helperfunc.open(get_config()['ENV']['url'])
        context.helperfunc.maximize()


def before_scenario(context, scenario):
    if "uiautomation" in context.feature.tags:
        context.helperfunc.find_by_xpath("//a[@href='/login']").click()
        context.helperfunc.find_by_name('user').send_keys(get_username())
        context.helperfunc.find_by_id('login').click()
        context.helperfunc.find_by_name('password').send_keys(get_password())
        context.helperfunc.find_by_id('login-submit').click()
        assert context.helperfunc.find_by_xpath("//span[text()='Workspaces']")


def after_scenario(context, scenario):
    if "uiautomation" in context.feature.tags:
        context.helperfunc.switch_to_main()
        context.helperfunc.find_by_xpath("//button[@data-testid='header-member-menu-button']").click()
        context.helperfunc.find_by_xpath("//span[text()='Log out']").click()
        context.helperfunc.find_by_xpath("//button[@id='logout-submit']").click()
        assert context.helperfunc.find_by_xpath("//a[@href='/login']")


def after_feature(context, feature):
    if "uiautomation" in context.feature.tags:
        context.helperfunc.close()

