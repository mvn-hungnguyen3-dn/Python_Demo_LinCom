from behave import given, when, then
from pages.medigo.home_page import home_page
from pages.medigo.login_page import login_page
from hamcrest import assert_that
import time


@when(u'Login application with username: "{username}" and password: "{password}"')
def step_impl(context, username, password):
    time.sleep(8)
    login_page.login(username, password)


@then(u'Verify message show "{expected_message}"')
def step_impl(context, expected_message):
    time.sleep(10)
    get_message = home_page.get_message()
    assert_that(get_message, expected_message, "Message is not found")
