from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def launch_odoo(context, user, pwd):
    context.driver = webdriver.Chrome(executable_path="C:\\Users\\Novel Tech Inc\\Downloads\\chromedriver.exe")
    context.driver.get("http://localhost:8069/")
    time.sleep(2)
    username_field = context.driver.find_element(By.ID, "login")
    username_field.send_keys(user)
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys(pwd)
    login_button = context.driver.find_element("xpath", "//button[@type='submit']")
    login_button.click()
    time.sleep(3)
