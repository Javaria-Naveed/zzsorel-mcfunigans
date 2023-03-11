from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import logintoodoo


def open_contacts(context):
    apps_button = context.driver.find_element("xpath", "/html/body/header/nav/div[1]/button/i")
    apps_button.click()
    ActionChains(context.driver).move_to_element(apps_button).perform()
    time.sleep(1)
    contacts_button = context.driver.find_element(By.LINK_TEXT, "Contacts")
    contacts_button.click()
    time.sleep(5)
    actual_text = context.driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div[1]/div[1]/ol/li/span").text
    assert actual_text == "Contacts"
