# FILE: iam_auth_login.py
# DESC: use Selenium with Python to automate auth login on E2E
from selenium import webdriver
from time import sleep

# ------------------------------------------------------------------------------
#                                  CONSTANTS
# ------------------------------------------------------------------------------
IAM_AUTH_URL_E2E = 'https://accounts-e2e.intuit.com/index.html?iux_v3=true'
TEST_USERNAME = 'iamtestpass_1581549935015'
TEST_USERPASS = 'Intuit01-'

# ------------------------------------------------------------------------------
#                            BROWSER-SPECIFIC WEB DRIVERS
# ------------------------------------------------------------------------------

# FIREFOX - geckodriver
browser = webdriver.Firefox()

# CHROME chromedriver (80)
# options = webdriver.ChromeOptions()
# options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# chrome_driver_binary = "/usr/local/bin/chromedriver"
# browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

# ------------------------------------------------------------------------------
#                                SCRIPT LOGIC
# ------------------------------------------------------------------------------

# Tests Auth Login on E2E
#
# 1. Start Flow with a GET for the URL
browser.get(IAM_AUTH_URL_E2E)

# Wait 10-20 Seconds for the Page to Load and DOM to be ready
# TODO: Replace this with WebDriver Wait utility method
sleep(10)

# Find User/Pass Elements and Enter Text
user_id_field = browser.find_element_by_id('ius-userid')
user_id_field.send_keys(TEST_USERNAME)
user_pass_field = browser.find_element_by_id('ius-password')
user_pass_field.send_keys(TEST_USERPASS)

# Click Sign-In Button
sign_in_button = browser.find_element_by_name('SignIn')
sign_in_button.click()

# Cleanup and Close Browser
# print("All is Good, About to close the browser")
# browser.close()
