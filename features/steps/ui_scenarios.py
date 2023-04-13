from behave import *
from helper.helper_base import *


@given(u'user opens the board')
def step_impl(context):
    context.helperfunc.find_by_xpath("//div/div[text()='ProjectTrello']").click()


@when(u'user navigates to create a automation rule')
def step_impl(context):
    context.helperfunc.find_by_xpath("//span[text()='Automation']").click()
    context.helperfunc.find_by_xpath("//div/span[text()='Rules']").click()
    time.sleep(5)


@when(u'user creates rule to add {color} label when new card is added')
def step_impl(context, color):
    context.helperfunc.switch_to_iframe("xpath", "//iframe[@class='butler-iframe']")
    context.helperfunc.find_by_xpath("//span/div[@class='rule']").click()
    context.helperfunc.find_by_xpath("//div[text()='+ Add Trigger']").click()
    time.sleep(5)
    context.helperfunc.find_and_choose_by_xpath("//form[text()=' when a card '][1]/div", 'created in', 'data-value')
    context.helperfunc.find_and_choose_by_xpath("//form[text()=' the board '][1]/span[2]/div", 'by anyone',
                                                'data-value')
    context.helperfunc.find_by_xpath("//form[text()=' when a card '][1]/button").click()

    context.helperfunc.find_by_xpath("//a[@data-tab='actions-card-add-remove']").click()
    context.helperfunc.find_and_choose_by_xpath("//div[@data-tab='actions-card-add-remove']/div[2]/div[2]", 'add',
                                                'data-value')
    context.helperfunc.find_and_choose_by_xpath("//div[@data-tab='actions-card-add-remove']/div[2]/div[3]", color,
                                                'data-value')
    context.helperfunc.find_by_xpath("//div[@data-tab='actions-card-add-remove']/div[2]/div[1]").click()


@when(u'user completes automation rule creation')
def step_impl(context):
    context.helperfunc.find_by_xpath("//div[text()=' Save ']").click()


@when(u'user creates a new card on the board with description {desc}')
def step_impl(context, desc):
    context.helperfunc.find_by_xpath("//div[div/textarea[text()='To Do']]/div/a/span[text()='Add a card']").click()
    context.helperfunc.find_by_xpath("//div[@class='card-composer']/div/div/textarea").send_keys(desc)
    context.helperfunc.find_by_xpath("//input[@value='Add card']").click()
    time.sleep(2)
    context.helperfunc.find_by_xpath("//span[text()='" + desc + "']").click()
    time.sleep(3)


@when(u'user deletes the {color} label rule added')
def step_impl(context, color):
    context.helperfunc.switch_to_iframe("xpath", "//iframe[@class='butler-iframe']")
    assert context.helperfunc. \
        find_by_xpath("//div[contains(text(),'when a card is created in the board by anyone')]")
    assert context.helperfunc. \
        find_by_xpath(
        "//div[div[h2[text()='Rules']]]/div/div/div/div[contains(text(),'add the " + color + " label to the card')]")

    context.helperfunc.find_by_xpath("//div[div[h2[text()='Rules']]]/div/div[div[div[contains(text(),'add the purple"
                                     " label to the card')]]]/div/div/div/div[@alt='Remove']/img").click()

    context.helperfunc.find_by_xpath("//div[text()=' Remove ']").click()


@then('A {color} color label is added in the card automatically')
def step_impl(context, color):
    assert context.helperfunc.verify_by_xpath("//div[h3[text()='Labels']]/div/button[@data-color='" + color + "']")
    context.helperfunc.find_by_xpath("//a[@aria-label='Close dialog']").click()
    time.sleep(2)


@then(u'the added {color} color label is displayed on the Rules page')
def step_impl(context, color):
    assert context.helperfunc. \
        find_by_xpath("//div[contains(text(),'when a card is created in the board by anyone')]")
    assert context.helperfunc. \
        find_by_xpath("//div[div[h2[text()='Rules']]]/div/div/div/div[contains(text(),'add the "
                      + color + " label to the card')]")


@then('the rule is successfully removed')
def step_impl(context):
    assert context.helperfunc. \
        find_by_xpath("//div[contains(text(),' Turn your Trello board into an automation machine. ')]")
