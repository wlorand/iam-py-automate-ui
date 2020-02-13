# FILE: iam_auth_login.py
# DESC: use Selenium with Python to automate auth login on E2E
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# ------------------------------------------------------------------------------
#                                  CONSTANTS
# ------------------------------------------------------------------------------
WAIT_TIMEOUT = 20 # in seconds
IAM_AUTH_URL_E2E = 'https://accounts-e2e.intuit.com/index.html?iux_v3=true'
TEST_USERNAME = 'iamtestpass_1581549935015' 
TEST_USERPASS = 'Intuit01-'

# ------------------------------------------------------------------------------
#                            BROWSER-SPECIFIC WEB DRIVERS
# ------------------------------------------------------------------------------

# FIREFOX - geckodriver
# browser = webdriver.Firefox()

# CHROME chromedriver (80)
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" 
chrome_driver_binary = "/usr/local/bin/chromedriver"
browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

# ------------------------------------------------------------------------------
#                                UTILITY METHODS
# ------------------------------------------------------------------------------

def wait_for_elem_select(selector):
    return WebDriverWait(browser, WAIT_TIMEOUT).until(lambda browser: browser.find_element_by_css_selector(selector))

# ------------------------------------------------------------------------------
#                                SCRIPT LOGIC
# ------------------------------------------------------------------------------

# Tests Auth Download Flow (No Products) on E2E
#
# 1. Login to Auth
# 2. Click Download: Start the Auth Flow 
# 3. Move thru the Download Flow Pages
browser.get(IAM_AUTH_URL_E2E)

# Enter User/Pass and Login
# user_id_field = browser.find_element_by_id('ius-userid')
# user_id_field.send_keys(TEST_USERNAME)
# user_pass_field = browser.find_element_by_id('ius-password')
# user_pass_field.send_keys(TEST_USERPASS)
wait_for_elem_select('#ius-userid').send_keys(TEST_USERNAME)
wait_for_elem_select('#ius-password').send_keys(TEST_USERPASS)
wait_for_elem_select('[name="SignIn"]').click()

# 2. Click Data and Privacy and then Download to Start Auth Flow 
# (selenium seems to need the element scrolled into view for firefox)
# wait_for_elem_select('button[data-automation="myData-sidenav-button]').click()
# wait_for_elem_select('button[data-automation="downloadManager-Continue-button"]').click()
WebDriverWait(browser, WAIT_TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-automation="downloadManager-Continue-button"]'))).click()

# 3. Move thru the Download Flow Pages
# Primer Page
wait_for_elem_select('button[data-automation="continue-button"]').click()

# Start Page
wait_for_elem_select('button[data-automation="continue-button"]').click()

# Confirm Page (No Products)
wait_for_elem_select('input[data-automation="password-field"]').send_keys(TEST_USERPASS)
wait_for_elem_select('button[data-automation="continue-button"]').click()

# Success Page
wait_for_elem_select('button[data-automation="done-button"]').click()


