# This File allows us to automate test case to test with First name only - written by Javaria-19L-1229

from behave import *
from selenium.webdriver.common.by import By
import time
import NavigatetoApp
import logintoodoo


@given('I am logged in')
def log_in(context):
    logintoodoo.launch_odoo(context, "javaria2912112@gmail.com", "pakistan555")


@given('I am on the contacts page')
def go_to_contacts_module(context):
    NavigatetoApp.open_app(context, "Contacts")


# Searching for first name "Azure"
@when('I enter a valid first name in the search bar')
def enter_first_name(context):
    search_bar = context.driver.find_element(By.CSS_SELECTOR, ".o_searchview_input")
    search_bar.click()
    search_bar.send_keys("addict")
    time.sleep(3)


@when('I click the search button')
def press_search_by_name(context):
    context.driver.find_element(By.LINK_TEXT, "Search Name for: addict").click()
    time.sleep(3)


@then('I should see a list of contacts matching the first name and the list should not contain any contacts with a '
      'different first name.')
def verify_search_results(context):
    results = context.driver.find_elements(By.CSS_SELECTOR, ".o_kanban_record_title")
    for result in results:
        assert "addict" in result.text.lower(), "Unexpected contact name in search results"
