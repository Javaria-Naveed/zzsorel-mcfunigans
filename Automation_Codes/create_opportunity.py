# This File allows us to automate test case to CREATE NEW OPPORTUNITY IN CRM - written by Javaria-19L-1229

from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import NavigatetoApp

# Define the selectors for the elements on the page
new_button_selector = ".btn-primary"
title_field_selector = "name"
add_button_selector = ".o_kanban_add"
opportunity_card_selector = ".o_content"


@given('I am on the Kanban view of the Odoo CRM module')
def navigate_to_crm(context):
    NavigatetoApp.open_app(context, "CRM")


@when('I click on the "New" button and enter "New Bakery Order" in the "Opportunity Title" field')
def click_new(context):
    # Click the "New" button
    new_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, new_button_selector)))
    new_button.click()

    # Enter the opportunity title
    title_field = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "name")))
    title_field.send_keys("New Bakery Order")


@when('I click the "Add" button')
def step_impl(context):
    add_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, add_button_selector)))
    add_button.click()
    time.sleep(3)


@then('a new opportunity with the title "New Bakery Order" should be created in the "New" stage of the Kanban view')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, opportunity_card_selector)))
    opportunity_cards = context.driver.find_elements(By.CSS_SELECTOR, opportunity_card_selector)
    for card in opportunity_cards:
        if "New Bakery Order" in card.text:
            assert "New" in card.text, "Opportunity was not created in the 'New' stage"
            return
    assert False, "Opportunity not found with title '{}'".format("New Bakery Order")
