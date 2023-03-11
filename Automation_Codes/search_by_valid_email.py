# This File allows us to automate test case to test with valid email only - written by Javaria-19L-1229

from behave import *
from selenium.webdriver.common.by import By
import time


@when('I enter a valid email address in the search bar')
def enter_email(context):
    search_bar = context.driver.find_element(By.CSS_SELECTOR, ".o_searchview_input")
    search_bar.click()
    search_bar.send_keys("jesse.brown74@example.com")
    time.sleep(3)


@when('I click the search by email button')
def click_search_button(context):
    context.driver.find_element(By.LINK_TEXT, "Search Email for: jesse.brown74@example.com").click()
    time.sleep(3)


@then('I should see a list of contacts matching the email address and list should not contain any contacts with a '
      'different email address')
def verify_search_results(context):
    results = context.driver.find_elements(By.CSS_SELECTOR, ".o_kanban_record_subtitle")
    for result in results:
        assert "jesse.brown74@example.com" in result.text.lower(), "Unexpected email address in search results"
