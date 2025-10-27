from behave import given, when, then
from app import verify_password
import re

@given('que el usuario ingresa una contraseña válida')
def step_given_valid_password(context):
    pass

@given('que el usuario no ingresa ninguna contraseña')
def step_given_empty_password(context):
    pass

@when('la contraseña es {password}')
def step_when_password(context, password):
    password = password.strip('"') if password != '""' else ""
    context.result = verify_password(password)

@then('el sistema debe devolver "{expected}"')
def step_then_result(context, expected):
    assert context.result == expected
