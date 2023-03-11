# file to automate navigation to contacts - by Javaria 19L1229

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import logintoodoo


def open_app(context, app):
    apps_button = context.driver.find_element(By.CSS_SELECTOR, ".oi-apps")
    apps_button.click()
    ActionChains(context.driver).move_to_element(apps_button).perform()
    time.sleep(1)
    contacts_button = context.driver.find_element(By.LINK_TEXT, app)
    contacts_button.click()
    time.sleep(5)
    if app == "Contacts":
        actual_text = context.driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div[1]/div[1]/ol/li/span").text
        assert actual_text == "Contacts"


