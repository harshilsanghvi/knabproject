import requests
from behave import *
from utilities.configuration import *
from utilities.resources import *
from utilities.payLoad import *


@given('the Card details of {name} {desc} {pos} and {due} for Trello Board')
def step_impl(context, name, desc, pos, due):
    context.url = get_config()['API']['endpoint'] + ApiResources.card
    print(context.url)
    context.createdcard_desc = desc
    context.headers = {"Accept": "application/json"}
    context.query = {"key": get_config()['CRED']['key'],
                     "token": get_config()['CRED']['token'],
                     "idList": "64089747ea26d174dbd2526e"}
    context.payLoad = addCardPayload(name, due, desc, pos)


@given('the new card with correct id')
def step_impl(context):
    context.url = get_config()['API']['endpoint'] + ApiResources.card + "/" + context.id
    context.query = {"key": get_config()['CRED']['key'],
                     "token": get_config()['CRED']['token']}
    context.headers = {"Accept": "application/json"}


@given('a card with incorrect id')
def step_impl(context):
    context.url = get_config()['API']['endpoint'] + ApiResources.card + "/pR7rasd"
    print(context.url)

    context.query = {"key": get_config()['CRED']['key'],
                     "token": get_config()['CRED']['token']}
    context.headers = {"Accept": "application/json"}
    print(context.query)


@given('a new Card with {name} and {due} is created in the Trello Board')
def step_impl(context, name, due):
    context.name = name
    context.url = get_config()['API']['endpoint'] + ApiResources.card
    context.headers = {"Accept": "application/json"}
    context.query = {"key": get_config()['CRED']['key'],
                     "token": get_config()['CRED']['token'],
                     "idList": "63f695a6ef5d968d9bd9cd0e"}
    context.payLoad = addCardPayload(name, due)
    context.response = requests.post(context.url, headers=context.headers, params=context.query, json=context.payLoad)
    response_json = context.response.json()
    context.id = response_json['id']


@given('updated desc value is {desc}')
def step_impl(context, desc):
    context.payLoad = updateCardPayload(desc)
    context.updated_card_desc = desc


@when('we execute the Get a Card API method')
def step_impl(context):
    context.response = requests.get(context.url, headers=context.headers, params=context.query, )


@when('we execute the Create a Card API method')
def step_impl(context):
    context.response = requests.post(context.url, headers=context.headers, params=context.query, json=context.payLoad, )


@when('we execute the Update a Card API method')
def step_impl(context):
    context.response = requests.put(context.url, headers=context.headers, params=context.query, json=context.payLoad, )


@when('we execute the Delete a Card API method')
def step_impl(context):
    context.response = requests.delete(context.url, headers=context.headers, params=context.query, )


@then('card details are successfully retrieved')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    context.id = response_json['id']
    assert response_json["name"] == context.name


@then('card desc is successfully updated')
def step_impl(context):
    response_json = context.response.json()
    context.desc = response_json['desc']
    assert response_json["desc"] == context.updated_card_desc


@then('card details are successfully deleted')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    assert response_json["limits"] == {}


@then('card is created successfully')
def step_impl(context):
    response_json = context.response.json()
    context.created_card_id = response_json['id']
    print("Id is ", context.created_card_id)
    assert response_json["desc"] == context.createdcard_desc


@then(u'status code of response is {statusCode:d}')
def step_impl(context, statusCode):
    assert context.response.status_code == statusCode
