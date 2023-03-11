# This File allows us to automate test case to test with First and Last name-written by Javaria-19L-1229
from behave import *
from selenium.webdriver.common.by import By
import time


@when('I enter a valid first name and last name in the search bar')
def enter_name(context):
    search_bar = context.driver.find_element(By.CSS_SELECTOR, ".o_searchview_input")
    search_bar.click()
    search_bar.send_keys("jesse brown")
    time.sleep(3)


@when('I click the search by name button')
def press_search_button(context):
    context.driver.find_element(By.LINK_TEXT, "Search Name for: jesse brown").click()
    time.sleep(3)


@then('I should see a list of contacts matching the first and last name and the list should not contain any contacts '
      'with a different first or last name')
def verify_search_results(context):
    results = context.driver.find_elements(By.CSS_SELECTOR, ".o_kanban_record_title")
    for result in results:
        assert "jesse brown" in result.text.lower(), "Unexpected contact name in search results"
