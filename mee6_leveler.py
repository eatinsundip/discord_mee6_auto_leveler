# https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver
# Download the selenium webdriver app and place it inside the directory of this script
# https://sites.google.com/a/chromium.org/chromedriver/
# make sure to pip install selenium and chromedriver_py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chromedriver_py import binary_path # this will get you the path variable
import time
import base64

# This script is not setup for an account with Multi Factor Authentication
email = '' # SET THIS
password_clear = '' # SET THIS
spam_message = '' # SET THIS
spam_message_lenth = len(atter)
# Make sure the account is already joined to the server you're having it sign in too.
ThaBestServer_bot-spam = 'https://discord.com/channels/254050713141903361/775873313279967272'

# Logs in and locates the main channel in thabestserver discord
def discord_login():
    driver = webdriver.Chrome(executable_path=binary_path)
    # opens the url 
    driver.get(ThaBestServer_bot-spam)
    driver.find_element_by_name("email").send_keys(email)
    time.sleep(1)
    driver.find_element_by_name("password").send_keys(str(password_clear)+'\n')
    time.sleep(3)
    while True:
        driver.switch_to_active_element().send_keys(spam_message)
        driver.switch_to_active_element().send_keys(Keys.ENTER)
        time.sleep(1)
        driver.switch_to_active_element().send_keys(Keys.ARROW_UP)
        time.sleep(1)
        driver.switch_to_active_element().send_keys(Keys.BACKSPACE*spam_message_lenth)
        time.sleep(1)
        driver.switch_to_active_element().send_keys(Keys.ENTER)
        time.sleep(1)
        driver.switch_to_active_element().send_keys(Keys.ENTER)
        time.sleep(56)


discord_login()
