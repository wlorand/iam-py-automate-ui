# FILE: iam_auth_login.py
# DESC: use Selenium with Python to automate auth login on E2E
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# ------------------------------------------------------------------------------
#                                  CONSTANTS
# ------------------------------------------------------------------------------
WAIT_TIMEOUT = 20 # seconds
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

# Tests Auth Login on E2E
browser.get(IAM_AUTH_URL_E2E)

# 1.1: Enter User/Pass
wait_for_elem_select('#ius-userid').send_keys(TEST_USERNAME)
wait_for_elem_select('#ius-password').send_keys(TEST_USERPASS)

# 1.2: Click Sign-In Button
wait_for_elem_select('button[name="SignIn"]').click()

# Cleanup 
print("All is Good, About to close the browser")
sleep(5)
browser.close()