# This File allows us to automate test case to test with valid phone no only - written by Javaria-19L-1229

from behave import *
from selenium.webdriver.common.by import By
import time


@when('I enter a valid phone number in the search bar')
def enter_phone_no(context):
    search_bar = context.driver.find_element(By.CSS_SELECTOR, ".o_searchview_input")
    search_bar.click()
    search_bar.send_keys("(225)-148-7811")
    time.sleep(3)


@when('I click the search by phone button')
def press_search_button(context):
    context.driver.find_element(By.LINK_TEXT, "Search Phone/Mobile for: (225)-148-7811").click()
    time.sleep(3)


@then('I should see a list of contacts matching the phone number and the list should not contain any contacts with a '
      'different phone number')
def verify_phone_no(context):
    results = context.driver.find_elements(By.CSS_SELECTOR, ".o_kanban_record")
    assert len(results) > 0, "No search results found"
    time.sleep(3)
    for result in results:
        result.click()
        time.sleep(3)
        phone_number = context.driver.find_element(By.ID, "phone").text
        assert phone_number == "(225)-148-7811", f'Incorrect phone number{phone_number} found for contact'
        context.driver.back()
