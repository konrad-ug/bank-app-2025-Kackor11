from behave import *
import requests

URL = "http://127.0.0.1:5000"

@step('I create an account using name: "{name}", last name: "{last_name}", pesel: "{pesel}"')
def create_account(context, name, last_name, pesel):
    json_body = {
        "name": name,
        "surname": last_name,
        "pesel": pesel
    }
    create_resp = requests.post(URL + "/api/accounts", json=json_body)
    context.last_status_code = create_resp.status_code
    assert create_resp.status_code == 201

@step('Account registry is empty')
def clear_account_registry(context):
    response = requests.get(URL + "/api/accounts")
    if response.status_code == 200:
        accounts = response.json()
        for account in accounts:
            pesel = account["pesel"]
            requests.delete(URL + f"/api/accounts/{pesel}")

@step('Number of accounts in registry equals: "{count}"')
def is_account_count_equal_to(context, count):
    response = requests.get(URL + "/api/accounts")
    accounts = response.json()
    assert len(accounts) == int(count)

@step('Account with pesel "{pesel}" exists in registry')
def check_account_with_pesel_exists(context, pesel):
    response = requests.get(URL + f"/api/accounts/{pesel}")
    assert response.status_code == 200

@step('Account with pesel "{pesel}" does not exist in registry')
def check_account_with_pesel_does_not_exist(context, pesel):
    response = requests.get(URL + f"/api/accounts/{pesel}")
    assert response.status_code == 404

@when('I delete account with pesel: "{pesel}"')
def delete_account(context, pesel):
    response = requests.delete(URL + f"/api/accounts/{pesel}")
    assert response.status_code == 200

@when('I update "{field}" of account with pesel: "{pesel}" to "{value}"')
def update_field(context, field, pesel, value):
    if field not in ["name", "surname"]:
        raise ValueError(f"Invalid field: {field}. Must be 'name' or 'surname'.")
    
    json_body = {field: value}
    response = requests.patch(URL + f"/api/accounts/{pesel}", json=json_body)
    assert response.status_code == 200

@then('Account with pesel "{pesel}" has "{field}" equal to "{value}"')
def field_equals_to(context, pesel, field, value):
    response = requests.get(URL + f"/api/accounts/{pesel}")
    assert response.status_code == 200
    data = response.json()
    
    api_value = data.get(field)
    
    if field == "balance":
        assert float(api_value) == float(value)
    else:
        assert str(api_value) == str(value)

# c. Przygotowane kroki i scenariusze na wykonywanie przelewów.

@step('I make an incoming transfer of "{amount}" to account with pesel "{pesel}"')
def make_incoming_transfer(context, amount, pesel):
    json_body = {
        "amount": float(amount),
        "type": "incoming"
    }
    response = requests.post(URL + f"/api/accounts/{pesel}/transfer", json=json_body)
    context.last_status_code = response.status_code

@step('I make an outgoing transfer of "{amount}" from account with pesel "{pesel}"')
def make_outgoing_transfer(context, amount, pesel):
    json_body = {
        "amount": float(amount),
        "type": "outgoing"
    }
    response = requests.post(URL + f"/api/accounts/{pesel}/transfer", json=json_body)
    context.last_status_code = response.status_code

@step('Request fails with status code {status_code}')
def check_status_code(context, status_code):
    assert context.last_status_code == int(status_code)