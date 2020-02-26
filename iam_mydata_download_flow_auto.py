# FILE: iam_auth_login.py
# DESC: use Selenium with Python to automate Download work order creation on E2E
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# ------------------------------------------------------------------------------
#                                  CONSTANTS
# ------------------------------------------------------------------------------
WAIT_TIMEOUT = 20 # seconds
IAM_AUTH_URL_E2E = 'https://accounts-e2e.intuit.com/index.html?iux_v3=true'
TEST_USERNAME = 'iamtestpass_1582582172775' # NOTE: This needs new test user for new request
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
browser.get(IAM_AUTH_URL_E2E)

# 1: Login to Auth
wait_for_elem_select('#ius-userid').send_keys(TEST_USERNAME)
wait_for_elem_select('#ius-password').send_keys(TEST_USERPASS)
wait_for_elem_select('button[name="SignIn"]').click()

# 2: Click Data & Privacy, Download 
WebDriverWait(browser, WAIT_TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-automation="downloadManager-Continue-button"]'))).click()

# 3: Move thru the Download Flow Pages
# 3.1: Primer Page
wait_for_elem_select('button[data-automation="continue-button"]').click()

# 3.2: Start Page
wait_for_elem_select('button[data-automation="continue-button"]').click()

# 3.3: Confirm Page (No Products)
wait_for_elem_select('input[data-automation="password-field"]').send_keys(TEST_USERPASS)
wait_for_elem_select('button[data-automation="continue-button"]').click()

# 3.4: Success Page
wait_for_elem_select('button[data-automation="done-button"]').click()
